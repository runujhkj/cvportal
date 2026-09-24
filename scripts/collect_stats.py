#!/usr/bin/env python3
"""Collect Forgejo repo stats for cvportal project pages.

Reads content/projects/*.md, resolves each project's Forgejo repo name
(uses frontmatter 'forgejo_repo' if set, otherwise the page slug), fetches
stats from the Forgejo API, and writes data/project_stats.json.

Required env vars:
  FORGEJO_TOKEN  — API token with read access to project repos

Optional env vars (defaults match the fed.home instance):
  FORGEJO_URL    — base URL of the Forgejo instance (default: https://fed.home)
  FORGEJO_USER   — Forgejo username owning the repos (default: thefed)
"""

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml is required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

FORGEJO_URL = os.environ.get("FORGEJO_URL", "https://fed.home")
FORGEJO_USER = os.environ.get("FORGEJO_USER", "thefed")
FORGEJO_TOKEN = os.environ.get("FORGEJO_TOKEN", "")

REPO_ROOT = Path(__file__).parent.parent
CONTENT_DIR = REPO_ROOT / "content" / "projects"
OUTPUT_FILE = REPO_ROOT / "data" / "project_stats.json"

SINCE_90D = (datetime.now(timezone.utc) - timedelta(days=90)).strftime(
    "%Y-%m-%dT%H:%M:%SZ"
)


def api_get(path):
    """Return (parsed_body, headers) for a Forgejo API GET, or (None, {}) on 404."""
    url = f"{FORGEJO_URL}/api/v1{path}"
    req = urllib.request.Request(url)
    if FORGEJO_TOKEN:
        req.add_header("Authorization", f"token {FORGEJO_TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read()), dict(resp.headers)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None, {}
        raise


def repo_stats(repo_name):
    """Return stats dict for one repo, or None if the repo is not found."""
    data, _ = api_get(f"/repos/{FORGEJO_USER}/{repo_name}")
    if data is None:
        return None

    _, h_all = api_get(
        f"/repos/{FORGEJO_USER}/{repo_name}/commits?limit=1&page=1"
    )
    _, h_90d = api_get(
        f"/repos/{FORGEJO_USER}/{repo_name}/commits?limit=1&page=1&since={SINCE_90D}"
    )

    return {
        "last_push": data.get("updated_at"),
        "commit_count": int(h_all.get("X-Total-Count", 0)),
        "commits_90d": int(h_90d.get("X-Total-Count", 0)),
    }


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    return yaml.safe_load(parts[1]) if len(parts) >= 3 else {}


def main():
    if not FORGEJO_TOKEN:
        print("warning: FORGEJO_TOKEN not set; requests to private repos will fail",
              file=sys.stderr)

    stats = {}
    errors = []

    for md_file in sorted(CONTENT_DIR.glob("*.md")):
        slug = md_file.stem
        if slug == "_index":
            continue
        fm = parse_frontmatter(md_file)
        repo_name = fm.get("forgejo_repo", slug)
        print(f"  {slug} → {repo_name} ... ", end="", flush=True)
        try:
            result = repo_stats(repo_name)
        except Exception as exc:
            print(f"error: {exc}")
            errors.append(slug)
            continue
        if result:
            stats[slug] = result
            print(f"ok  (last push {(result['last_push'] or '?')[:10]}, "
                  f"{result['commit_count']} commits, "
                  f"{result['commits_90d']} in 90d)")
        else:
            print("not found in Forgejo, skipping")

    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
    print(f"\nWrote {len(stats)} entries → {OUTPUT_FILE.relative_to(REPO_ROOT)}")

    if errors:
        print(f"Errors on: {', '.join(errors)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
