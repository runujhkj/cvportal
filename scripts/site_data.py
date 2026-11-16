#!/usr/bin/env python3
"""Write the small, public data files the site shows, from local sources.

  data/project_activity.json  last commit date per project page, from facts/ (run `make facts` first)
  data/vplan_tunnel.json      weekly WireGuard tunnel reliability, from vplan's watchdog tally

Only dates and counts are written: no repo names beyond page slugs, no hostnames, no paths.
"""

import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FACTS = ROOT / "facts"
DATA = ROOT / "data"
TUNNEL_STATS = Path(os.environ.get(
    "VPLAN_WD_STATS", Path.home() / "Library" / "Application Support" / "vplan" / "wg-watchdog-stats.tsv"))
CHECK_SECONDS = 10  # the watchdog checks the tunnel every 10 s while away from home
MIN_WEEK_HOURS = 10  # a week with less time on the tunnel is too small a sample to chart


def last_commit(facts):
    last = (facts.get("commits") or {}).get("last")
    if not last:  # Forgejo-only repos: the newest of its recent commits and its last push
        dates = [c[:10] for c in facts.get("recent_commits") or []]
        dates.append(((facts.get("forgejo") or {}).get("updated_at") or "")[:10])
        last = max(dates) or None
    return last


def project_activity():
    if not list(FACTS.glob("*.json")):
        print("no facts/ yet: run `make facts` first; skipping project activity", file=sys.stderr)
        return
    activity = {}
    for path in FACTS.glob("*.json"):
        facts = json.loads(path.read_text())
        slug, last = (facts.get("page") or {}).get("slug"), last_commit(facts)
        if slug and last:
            activity[slug] = max(last, activity.get(slug, ""))
    write("project_activity.json", dict(sorted(activity.items())))


def vplan_tunnel():
    if not TUNNEL_STATS.is_file():
        print(f"no tunnel stats at {TUNNEL_STATS}; skipping", file=sys.stderr)
        return
    weeks = {}
    for line in TUNNEL_STATS.read_text().splitlines():
        day, ok, stalled, restarts = line.split("\t")[:4]
        d = date.fromisoformat(day)
        week = weeks.setdefault(d - timedelta(days=d.weekday()), {"first": d, "last": d, "ok": 0, "stalled": 0, "restarts": 0})
        week["first"], week["last"] = min(week["first"], d), max(week["last"], d)
        week["ok"] += int(ok)
        week["stalled"] += int(stalled)
        week["restarts"] += int(restarts)
    rows = []
    for w in (weeks[k] for k in sorted(weeks)):
        checks = w["ok"] + w["stalled"]
        if not checks:
            continue
        hours = checks * CHECK_SECONDS / 3600
        if hours < MIN_WEEK_HOURS:
            continue
        first, last = w["first"], w["last"]
        if first == last:
            label = f"{first:%b} {first.day}"
        elif first.month == last.month:
            label = f"{first:%b} {first.day}–{last.day}"
        else:
            label = f"{first:%b} {first.day}–{last:%b} {last.day}"
        rows.append({
            "week_of": f"{w['first']:%b} {w['first'].day}",
            "label": label,
            "hours": round(hours, 1),
            "available_pct": round(w["ok"] * 100 / checks, 2),
            "stalled_min_per_hour": round(w["stalled"] * CHECK_SECONDS / 60 / hours, 2),
            "restarts_per_hour": round(w["restarts"] / hours, 2),
        })
    write("vplan_tunnel.json", {"weeks": rows})


def write(name, payload):
    DATA.mkdir(exist_ok=True)
    (DATA / name).write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote data/{name}")


if __name__ == "__main__":
    project_activity()
    vplan_tunnel()
