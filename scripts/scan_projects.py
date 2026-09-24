#!/usr/bin/env python3
"""Report local and Forgejo repos that are candidates for new or updated cvportal pages.

Env: PROJECTS_DIR (default ~/projects), STALE_DAYS (default 14),
FORGEJO_TOKEN / FORGEJO_URL / FORGEJO_USER (Forgejo section runs only if a token is set).
"""

import json
import os
import re
import subprocess
import urllib.request
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = REPO_ROOT / "content" / "projects"
PROJECTS_DIR = Path(os.environ.get("PROJECTS_DIR", "~/projects")).expanduser()
STALE_DAYS = int(os.environ.get("STALE_DAYS", "14"))
FORGEJO_URL = os.environ.get("FORGEJO_URL", "https://fed.home")
FORGEJO_USER = os.environ.get("FORGEJO_USER", "thefed")
FORGEJO_TOKEN = os.environ.get("FORGEJO_TOKEN", "")


def git(repo, *args):
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def page_map():
    """Map lowercase repo name -> page slug, honoring forgejo_repo overrides."""
    mapping = {}
    for md in PAGES_DIR.glob("*.md"):
        if md.stem == "_index":
            continue
        m = re.search(r'^forgejo_repo:\s*"?([^"\n]+)"?\s*$', md.read_text(encoding="utf-8"), re.M)
        mapping[(m.group(1) if m else md.stem).lower()] = md.stem
    return mapping


def days_between(a, b):
    return (date.fromisoformat(a) - date.fromisoformat(b)).days


def local_rows(pages, me):
    rows = []
    for d in sorted(p for p in PROJECTS_DIR.iterdir() if (p / ".git").exists()):
        if d.resolve() == REPO_ROOT:
            continue
        last = git(d, "log", "-1", "--format=%cs")
        if not last:
            rows.append((d.name, "", "", "", "", "-", "empty repo, no commits"))
            continue
        total = int(git(d, "rev-list", "--count", "HEAD"))
        recent = int(git(d, "rev-list", "--count", "--since=90.days", "HEAD"))
        mine = int(git(d, "rev-list", "--count", f"--author={me}", "HEAD")) if me else total
        slug = pages.get(d.name.lower())
        notes = []
        if mine < total / 2:
            top = git(d, "shortlog", "-se", "HEAD").splitlines()
            who = max(top, key=lambda l: int(l.split()[0])).split(None, 1)[1] if top else "?"
            notes.append(f"mostly authored by {who}")
        if slug:
            edited = git(REPO_ROOT, "log", "-1", "--format=%cs", "--", f"content/projects/{slug}.md")
            if edited and days_between(last, edited) > STALE_DAYS:
                notes.append(f"STALE: repo {days_between(last, edited)}d newer than page")
        elif recent and mine >= total / 2:
            notes.append("NEW? active, no page")
        rows.append((d.name, last, str(recent), str(total), str(mine), slug or "NONE", "; ".join(notes)))
    return sorted(rows, key=lambda r: r[1], reverse=True)


def forgejo_rows(pages, local_names):
    req = urllib.request.Request(f"{FORGEJO_URL}/api/v1/users/{FORGEJO_USER}/repos?limit=50")
    req.add_header("Authorization", f"token {FORGEJO_TOKEN}")
    with urllib.request.urlopen(req, timeout=15) as resp:
        repos = json.loads(resp.read())
    rows = []
    for r in repos:
        if r["name"].lower() in local_names:
            continue
        rows.append((r["name"], (r.get("updated_at") or "")[:10],
                     pages.get(r["name"].lower(), "NONE"), r.get("description") or ""))
    return sorted(rows, key=lambda r: r[1], reverse=True), {r["name"].lower() for r in repos}


def table(header, rows):
    widths = [max(len(str(x)) for x in col) for col in zip(header, *rows)]
    for row in (header, *rows):
        print("  ".join(str(x).ljust(w) for x, w in zip(row, widths)).rstrip())


def main():
    pages = page_map()
    me = git(REPO_ROOT, "config", "user.email")
    rows = local_rows(pages, me)
    print(f"Local repos in {PROJECTS_DIR} (90D = commits in last 90 days, MINE = authored by {me or '?'})\n")
    table(("REPO", "LAST", "90D", "TOTAL", "MINE", "PAGE", "NOTE"), rows)

    found = {r[0].lower() for r in rows}
    if FORGEJO_TOKEN:
        print(f"\nForgejo repos at {FORGEJO_URL} not cloned locally\n")
        try:
            remote, remote_names = forgejo_rows(pages, found)
            table(("REPO", "UPDATED", "PAGE", "DESCRIPTION"), remote)
            found |= remote_names
        except Exception as exc:
            print(f"  skipped: {exc}")
    else:
        print("\n(FORGEJO_TOKEN not set; skipping Forgejo listing)")

    orphans = sorted(slug for repo, slug in pages.items() if repo not in found)
    if orphans:
        print(f"\nPages with no repo found: {', '.join(orphans)}")


if __name__ == "__main__":
    main()
