#!/usr/bin/env python3
"""Collect mechanical facts about project repos into facts/ (untracked, local only).

Sources: git repos under PROJECTS_DIR (default ~/projects) and, when a Forgejo
token is available (see scripts/forgejo.py), the Forgejo instance, including
repos that are not cloned locally. Writes facts/<repo>.json and facts/DIGEST.md.

Nothing here is published: facts/ is gitignored because it holds commit
messages, hostnames and other details from private repos.
"""

import json
import os
import re
import subprocess
import sys
import tomllib
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forgejo  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = REPO_ROOT / "content" / "projects"
OUT_DIR = REPO_ROOT / "facts"
PROJECTS_DIR = Path(os.environ.get("PROJECTS_DIR", "~/projects")).expanduser()

LANGS = {
    ".py": "Python", ".sh": "Shell", ".bash": "Shell", ".zsh": "Shell", ".swift": "Swift",
    ".cs": "C#", ".js": "JavaScript", ".jsx": "JavaScript", ".mjs": "JavaScript",
    ".ts": "TypeScript", ".tsx": "TypeScript", ".c": "C", ".h": "C/C++ header",
    ".cpp": "C++", ".cc": "C++", ".hpp": "C++", ".go": "Go", ".rs": "Rust",
    ".html": "HTML", ".css": "CSS", ".sql": "SQL", ".md": "Markdown",
}
TEST_RE = re.compile(
    r"(^|/)(tests?|Tests|__tests__)/[^/]+\.(py|swift|cs|js|ts|tsx)$"
    r"|(^|/)test_[^/]+\.py$|_test\.(py|go)$|\.(test|spec)\.(js|jsx|ts|tsx)$|Tests?\.(swift|cs)$"
)
MARKERS = {
    "readme": r"^README[^/]*$", "license": r"^(LICENSE|COPYING)[^/]*$",
    "dockerfile": r"(^|/)Dockerfile[^/]*$", "compose": r"(^|/)(docker-)?compose[^/]*\.ya?ml$",
    "makefile": r"^Makefile$", "forgejo_ci": r"^\.forgejo/workflows/", "github_ci": r"^\.github/workflows/",
    "pyproject": r"^pyproject\.toml$", "requirements": r"^requirements[^/]*\.txt$",
    "package_json": r"(^|/)package\.json$", "swift_package": r"^Package\.swift$",
    "xcode": r"\.xcodeproj/", "unity": r"^ProjectSettings/ProjectVersion\.txt$",
}


def git(repo, *args):
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, errors="replace")
    return r.stdout.strip() if r.returncode == 0 else ""


def own_authors():
    """Author patterns that count as the owner: git name and email, plus CVPORTAL_AUTHORS (comma-separated)."""
    names = [git(REPO_ROOT, "config", "user.email"), git(REPO_ROOT, "config", "user.name")]
    names += os.environ.get("CVPORTAL_AUTHORS", "").split(",")
    return [n.strip() for n in names if n.strip()]


def page_map():
    mapping = {}
    for md in PAGES_DIR.glob("*.md"):
        if md.stem == "_index":
            continue
        m = re.search(r'^forgejo_repo:\s*"?([^"\n]+)"?\s*$', md.read_text(encoding="utf-8"), re.M)
        mapping[(m.group(1) if m else md.stem).lower()] = md.stem
    return mapping


def excerpt(text, max_lines=40, max_chars=1800):
    lines = [l.rstrip() for l in text.splitlines() if l.strip()][:max_lines]
    return "\n".join(lines)[:max_chars]


def dependencies(repo, files):
    deps = []
    for f in files:
        path = repo / f
        try:
            if re.match(r"^requirements[^/]*\.txt$", f):
                deps += [re.split(r"[<>=!~\[; ]", l.strip())[0] for l in path.read_text().splitlines()
                         if l.strip() and not l.lstrip().startswith(("#", "-"))]
            elif f == "pyproject.toml":
                data = tomllib.loads(path.read_text())
                deps += [re.split(r"[<>=!~\[; ]", d)[0] for d in data.get("project", {}).get("dependencies", [])]
            elif f.endswith("package.json") and "node_modules" not in f:
                data = json.loads(path.read_text())
                deps += list(data.get("dependencies", {})) + list(data.get("devDependencies", {}))
        except (OSError, ValueError):
            continue
    return sorted({d for d in deps if d})[:50]


def local_facts(repo, pages, me):
    name = repo.name
    facts = {"name": name, "source": "local", "path": str(repo)}
    last = git(repo, "log", "-1", "--format=%cs")
    if not last:
        facts["kind"] = "empty"
        return facts

    total = int(git(repo, "rev-list", "--count", "HEAD"))
    mine = int(git(repo, "rev-list", "--count", *[f"--author={a}" for a in me], "HEAD")) if me else total
    authors = [l.strip() for l in git(repo, "shortlog", "-sne", "HEAD").splitlines()][:5]
    top = authors[0] if authors else ""
    if mine >= total / 2:
        kind = "own"
    elif "locallm@localhost" in top:
        kind = "locallm-generated"
    else:
        kind = "upstream-clone"

    months = Counter(d[:7] for d in git(repo, "log", "--since=12.months", "--format=%cs").splitlines())
    facts.update({
        "kind": kind,
        "commits": {
            "total": total, "mine": mine, "last_90d": int(git(repo, "rev-list", "--count", "--since=90.days", "HEAD")),
            "first": git(repo, "log", "--reverse", "--format=%cs").splitlines()[0], "last": last,
            "by_month_last_12": dict(sorted(months.items())),
        },
        "authors": authors,
        "remotes": sorted(set(git(repo, "remote", "-v").replace("\t", " ").replace(" (fetch)", "").replace(" (push)", "").splitlines())),
        "tags": git(repo, "tag", "--sort=-creatordate").splitlines()[:10],
    })
    if kind == "upstream-clone":
        return facts

    files = [f for f in git(repo, "ls-files").splitlines() if f]
    loc, test_files = Counter(), 0
    for f in files:
        if TEST_RE.search(f):
            test_files += 1
        lang = LANGS.get(Path(f).suffix.lower())
        path = repo / f
        if not lang or not path.is_file() or path.stat().st_size > 1_000_000:
            continue
        with open(path, "rb") as fh:
            loc[lang] += fh.read().count(b"\n")

    readme = next((f for f in files if re.match(r"^README(\.md|\.txt|\.rst)?$", f, re.I)), None)
    docs = [f for f in files if f.lower().endswith(".md") and (f.count("/") == 0 or f.startswith("docs/"))]
    slug = pages.get(name.lower()) or pages.get(forgejo.repo_name_from_remotes(facts["remotes"]).lower())
    edited = git(REPO_ROOT, "log", "-1", "--format=%cs", "--", f"content/projects/{slug}.md") if slug else ""
    unity = repo / "ProjectSettings" / "ProjectVersion.txt"
    facts.update({
        "tracked_files": len(files),
        "lines_by_language": dict(loc.most_common()),
        "test_files": test_files,
        "markers": sorted(k for k, rx in MARKERS.items() if any(re.search(rx, f) for f in files)),
        "unity_version": unity.read_text().splitlines()[0].split(":")[-1].strip() if unity.is_file() else None,
        "dependencies": dependencies(repo, [f for f in files if re.search(r"(requirements[^/]*\.txt|pyproject\.toml|package\.json)$", f)]),
        "docs": {f: sum(1 for _ in open(repo / f, errors="replace")) for f in docs[:40] if (repo / f).is_file()},
        "readme_excerpt": excerpt((repo / readme).read_text(errors="replace")) if readme else "",
        "recent_commits": git(repo, "log", "-25", "--no-merges", "--format=%cs %s").splitlines(),
        "page": {"slug": slug, "last_edited": edited,
                 "repo_days_newer": (date.fromisoformat(last) - date.fromisoformat(edited)).days if edited else None},
    })
    return facts


def forgejo_only_facts(r):
    full = r["full_name"]
    facts = {"name": r["name"], "source": "forgejo-only", "kind": "own"}
    langs, _ = forgejo.get(f"/repos/{full}/languages")
    _, headers = forgejo.get(f"/repos/{full}/commits?limit=1&stat=false&verification=false&files=false")
    commits, _ = forgejo.get(f"/repos/{full}/commits?limit=25&stat=false&verification=false&files=false")
    readme, _ = forgejo.get(f"/repos/{full}/raw/README.md", raw=True)
    facts.update({
        "commits": {"total": int(headers.get("x-total-count", 0))},
        "bytes_by_language": langs or {},
        "readme_excerpt": excerpt(readme or ""),
        "recent_commits": [f"{c['commit']['author']['date'][:10]} {c['commit']['message'].splitlines()[0]}"
                           for c in (commits or [])],
    })
    return facts


def forgejo_meta(r):
    return {k: r.get(k) for k in ("description", "private", "archived", "empty", "created_at", "updated_at",
                                  "default_branch", "size", "topics", "open_issues_count", "release_counter")}


def digest(all_facts):
    out = [f"# Project facts digest ({date.today().isoformat()})", "",
           "Local only. Do not commit or publish: contains details from private repos.", "",
           "| Repo | Kind | Source | Commits | 90d | First | Last | Main languages (lines) | Tests | Page |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    ordered = sorted(all_facts, key=lambda f: f.get("commits", {}).get("last", f.get("forgejo", {}).get("updated_at") or ""), reverse=True)
    for f in ordered:
        c = f.get("commits", {})
        langs = ", ".join(f"{k} {v:,}" for k, v in list(f.get("lines_by_language", {}).items())[:3])
        page = (f.get("page") or {}).get("slug") or "-"
        out.append(f"| {f['name']} | {f.get('kind', '')} | {f['source']}{' +forgejo' if f.get('forgejo') and f['source'] == 'local' else ''} "
                   f"| {c.get('total', '')} | {c.get('last_90d', '')} | {c.get('first', '')} | {c.get('last', '')} | {langs} | {f.get('test_files', '')} | {page} |")
    for f in ordered:
        if f.get("kind") in ("empty", "upstream-clone"):
            continue
        out += ["", f"## {f['name']}", ""]
        fj = f.get("forgejo") or {}
        if fj.get("description"):
            out.append(f"- Forgejo description: {fj['description']}")
        if fj.get("name") and fj["name"] != f["name"]:
            out.append(f"- Forgejo repo name: {fj['name']}")
        if fj:
            out.append(f"- Forgejo: private={fj.get('private')}, archived={fj.get('archived')}, updated {str(fj.get('updated_at'))[:10]}")
        for key, label in (("authors", "Authors"), ("markers", "Has"), ("dependencies", "Dependencies"), ("tags", "Tags")):
            if f.get(key):
                out.append(f"- {label}: {', '.join(f[key])}")
        if f.get("unity_version"):
            out.append(f"- Unity: {f['unity_version']}")
        if f.get("lines_by_language"):
            out.append("- Lines: " + ", ".join(f"{k} {v:,}" for k, v in f["lines_by_language"].items()))
        if f.get("bytes_by_language"):
            out.append("- Bytes by language: " + ", ".join(f"{k} {v:,}" for k, v in f["bytes_by_language"].items()))
        if f.get("commits", {}).get("by_month_last_12"):
            out.append("- Commits by month: " + ", ".join(f"{k}: {v}" for k, v in f["commits"]["by_month_last_12"].items()))
        page = f.get("page") or {}
        if page.get("slug"):
            out.append(f"- Page: {page['slug']} (edited {page['last_edited']}; repo {page['repo_days_newer']}d newer)")
        if f.get("docs"):
            out.append("- Docs: " + ", ".join(f"{k} ({v})" for k, v in f["docs"].items()))
        if f.get("readme_excerpt"):
            out += ["", "README excerpt:", "", "```", f["readme_excerpt"], "```"]
        if f.get("recent_commits"):
            out += ["", "Recent commits:", ""] + [f"- {c}" for c in f["recent_commits"]]
    return "\n".join(out) + "\n"


def main():
    pages = page_map()
    me = own_authors()
    OUT_DIR.mkdir(exist_ok=True)
    all_facts = []

    for repo in sorted(p for p in PROJECTS_DIR.iterdir() if (p / ".git").exists()):
        if repo.resolve() == REPO_ROOT:
            continue
        print(f"  local    {repo.name}", flush=True)
        all_facts.append(local_facts(repo, pages, me))

    if forgejo.token():
        try:
            remote = forgejo.get_all("/user/repos")
        except forgejo.ApiError as exc:
            remote = []
            print(f"Forgejo skipped: {exc}", file=sys.stderr)
        by_name = {f["name"].lower(): f for f in all_facts}
        # A local clone may be pushed under a different name; trust its remote URL.
        for f in all_facts:
            pushed_as = forgejo.repo_name_from_remotes(f.get("remotes", []))
            if pushed_as:
                f["forgejo_name"] = pushed_as
                by_name.setdefault(pushed_as.lower(), f)
        for r in remote:
            if r["name"].lower() == REPO_ROOT.name.lower():
                continue
            if r["name"].lower() in by_name:
                by_name[r["name"].lower()]["forgejo"] = {"name": r["name"], **forgejo_meta(r)}
                continue
            print(f"  forgejo  {r['name']}", flush=True)
            try:
                facts = forgejo_only_facts(r)
            except forgejo.ApiError as exc:
                facts = {"name": r["name"], "source": "forgejo-only", "kind": "own", "error": str(exc)}
            facts["forgejo"] = forgejo_meta(r)
            slug = pages.get(r["name"].lower())
            facts["page"] = {"slug": slug, "last_edited": "", "repo_days_newer": None}
            all_facts.append(facts)
    else:
        print("No Forgejo token found; local repos only. See scripts/forgejo.py.", file=sys.stderr)

    for stale in OUT_DIR.glob("*.json"):
        stale.unlink()
    for f in all_facts:
        (OUT_DIR / f"{f['name']}.json").write_text(json.dumps(f, indent=2) + "\n", encoding="utf-8")
    (OUT_DIR / "DIGEST.md").write_text(digest(all_facts), encoding="utf-8")
    print(f"\nWrote {len(all_facts)} repo files and DIGEST.md to {OUT_DIR.relative_to(REPO_ROOT)}/ (untracked)")


if __name__ == "__main__":
    main()
