#!/usr/bin/env python3
"""Cover letters and an application tracker, all under the gitignored private/applications/.

  letters.py new COMPANY TITLE   make private/applications/<company>/<title>/ with job.toml and letter.md
  letters.py build [FOLDER...]   build each letter.md into cover-letter.pdf beside it, styled like the resumes
  letters.py list                print the tracker and write private/applications/INDEX.md

letter.md holds only the body you paste in. The header (name, address, phone, email),
date, company, role line, greeting and sign-off come from job.toml, data/contact.toml
and private/contact.toml.
"""

import os
import re
import subprocess
import sys
import tempfile
import tomllib
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPS = Path(os.environ.get("CVPORTAL_APPLICATIONS", ROOT / "private" / "applications"))
PRIVATE_CONTACT = Path(os.environ.get("CVPORTAL_PRIVATE_CONTACT", ROOT / "private" / "contact.toml"))
HTML2PDF = ROOT / "build" / "html2pdf"
CSS = [ROOT / "static" / "resume" / "resume.css", ROOT / "scripts" / "letter.css"]
STATUSES = ("drafted", "applied", "interviewing", "offer", "rejected", "withdrawn")
BODY_MARKER = "<!-- Paste the body of the letter below this line. -->"

JOB_TEMPLATE = '''# One application. Edit freely; `make applications` reads this file.
company = "{company}"
title = "{title}"
created = {today}
status = "drafted"        # {statuses}
applied = ""              # date you sent it, e.g. "2026-11-10"
resume = ""               # which resume variant you sent: automation, hpc, hardware, logistics
link = ""                 # job posting URL
recipient = ""            # a named person, if the posting gives one
greeting = "Dear Hiring Manager,"
letter_date = ""          # date printed on the letter; empty means the day it is built
contact = "phone,email"   # fields from data/contact.toml under your name and address
notes = ""
'''

LETTER_TEMPLATE = f"""<!-- Cover letter body for {{company}}, {{title}}.
The header, date, role line, greeting and sign-off are added when it is built;
write only the paragraphs. Each line is a paragraph unless you use blank lines
between paragraphs, in which case normal Markdown rules apply. -->
{BODY_MARKER}

"""


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "untitled"


def rel(path):
    return path.relative_to(ROOT) if path.is_relative_to(ROOT) else path


def load_toml(path):
    return tomllib.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}


def jobs():
    return sorted(p.parent for p in APPS.glob("*/*/job.toml"))


def cmd_new(company, title):
    folder = APPS / slug(company) / slug(title)
    if (folder / "job.toml").exists():
        sys.exit(f"already exists: {rel(folder)}")
    folder.mkdir(parents=True, exist_ok=True)
    esc = lambda s: s.replace("\\", "\\\\").replace('"', '\\"')
    (folder / "job.toml").write_text(JOB_TEMPLATE.format(
        company=esc(company), title=esc(title), today=date.today().isoformat(), statuses=", ".join(STATUSES)))
    (folder / "letter.md").write_text(LETTER_TEMPLATE.format(company=company, title=title))
    print(f"created {rel(folder)}/  (paste the letter into letter.md, then: make letters)")


def letter_markdown(folder):
    job = load_toml(folder / "job.toml")
    contact = load_toml(ROOT / "data" / "contact.toml")
    address = load_toml(PRIVATE_CONTACT).get("address", "").strip()
    if "FILL IN" in address:
        address = ""
    raw = (folder / "letter.md").read_text(encoding="utf-8")
    body = raw.split(BODY_MARKER, 1)[-1].strip()
    if not body:
        return None
    if "\n\n" not in body:
        # Pasted text usually separates paragraphs with single line breaks, which
        # Markdown would join into one block; treat each line as a paragraph.
        body = "\n\n".join(line.strip() for line in body.splitlines() if line.strip())
    fields = [f.strip() for f in job.get("contact", "phone,email").split(",") if f.strip()]
    contact_line = " · ".join(str(contact[f]) for f in fields if contact.get(f) and f != "address")
    when = job.get("letter_date") or date.today()
    if not isinstance(when, date):
        when = date.fromisoformat(str(when))
    to = [l for l in (job.get("recipient", ""), job.get("company", "")) if l]
    lines = [
        f"# {contact.get('name', '')}", "",
        *( [f"{address}  "] if address else [] ), contact_line, "", "---", "",
        f"{when:%B} {when.day}, {when.year}", "",
        "  \n".join(to), "",
        f"**Re: {job.get('title', '')}**", "",
        job.get("greeting", "Dear Hiring Manager,"), "",
        body, "",
        "Sincerely,", "",
        contact.get("signature", contact.get("name", "")), "",
    ]
    return "\n".join(lines)


def cmd_build(folders):
    if not HTML2PDF.exists():
        sys.exit("build/html2pdf missing: run through `make letters`")
    targets = [Path(f).resolve() for f in folders] if folders else jobs()
    built = 0
    with tempfile.TemporaryDirectory() as tmp:
        for folder in targets:
            md = letter_markdown(folder)
            if md is None:
                print(f"skipped {rel(folder)}/ (letter.md has no body yet)")
                continue
            src, html = Path(tmp, "letter.md"), Path(tmp, "letter.html")
            src.write_text(md, encoding="utf-8")
            css = [arg for c in CSS for arg in ("--css", str(c))]
            subprocess.run(["pandoc", str(src), "-o", str(html), "--from", "markdown", "--standalone",
                            "--embed-resources", *css, "-M", "pagetitle=Cover letter"], check=True)
            subprocess.run([str(HTML2PDF), str(html), str(folder / "cover-letter.pdf"), "0.9", "1"], check=True)
            print(f"built {rel(folder)}/cover-letter.pdf")
            built += 1
    cmd_list(quiet=True)
    return built


def cmd_list(quiet=False):
    rows = []
    for folder in jobs():
        job = load_toml(folder / "job.toml")
        pdf = folder / "cover-letter.pdf"
        rows.append((str(job.get("created", "")), str(job.get("applied", "")) or "-", job.get("status", ""),
                     job.get("company", ""), job.get("title", ""), job.get("resume", "") or "-",
                     "yes" if pdf.exists() else "no", str(folder.relative_to(APPS))))
    rows.sort(key=lambda r: r[0], reverse=True)
    header = ("Created", "Applied", "Status", "Company", "Title", "Resume", "Letter", "Folder")
    APPS.mkdir(parents=True, exist_ok=True)
    md = ["# Applications", "", "Generated by `make applications`; edit each job.toml, not this file.", "",
          "| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    md += ["| " + " | ".join(r) + " |" for r in rows]
    (APPS / "INDEX.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    if quiet:
        return
    if not rows:
        print("No applications yet. Start one with: make letter COMPANY=\"...\" TITLE=\"...\"")
        return
    widths = [max(len(x) for x in col) for col in zip(header, *rows)]
    for row in (header, *rows):
        print("  ".join(x.ljust(w) for x, w in zip(row, widths)).rstrip())
    counts = {s: sum(1 for r in rows if r[2] == s) for s in STATUSES}
    print("\n" + ", ".join(f"{n} {s}" for s, n in counts.items() if n))


def main():
    args = sys.argv[1:]
    if not args or args[0] not in ("new", "build", "list"):
        sys.exit(__doc__)
    if args[0] == "new":
        if len(args) != 3 or not all(a.strip() for a in args[1:]):
            sys.exit('usage: make letter COMPANY="Company" TITLE="Job title"')
        cmd_new(args[1].strip(), args[2].strip())
    elif args[0] == "build":
        cmd_build(args[1:])
    else:
        cmd_list()


if __name__ == "__main__":
    main()
