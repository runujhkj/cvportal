#!/usr/bin/env bash
# Builds every resume to PDF with one renderer: contact placeholders filled from
# data/contact.toml, pandoc to standalone HTML, then the system WebKit
# (scripts/html2pdf.swift) to US Letter PDF.
#
# Each PDF is named after the person (e.g. Jeffrey-Hannon-Jr-Resume.pdf, from the
# signature in data/contact.toml), so every variant gets its own folder.
#
# Normal build: public variants come from content/ and land in static/resume/<variant>/,
# where the site links to them; private variants come from the gitignored private/
# folder and land in private/resumes/<variant>/. No postal address is ever included.
#
# --share: every variant, public and private, is built with the postal address from
# private/contact.toml into private/share/<variant>/ (gitignored), for sending to one person.
set -euo pipefail
cd "$(dirname "$0")/.."
html2pdf=${1:-build/html2pdf}
mode=${2:-}
css=static/resume/resume.css
pdf=$(python3 -c 'import tomllib; c = tomllib.load(open("data/contact.toml", "rb")); print(c["signature"].replace(".", "").replace(" ", "-"))')-Resume.pdf
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

address_flag=""
if [ "$mode" = "--share" ]; then
  address_flag="--with-address"
fi

build() {  # variant source output-root
  local md="$tmp/$1.md" html="$tmp/$1.html" out="$3/$1"
  [ -n "$address_flag" ] && out=private/share/$1
  mkdir -p "$out"
  python3 scripts/expand_contact.py "$2" $address_flag > "$md"
  pandoc "$md" -o "$html" --from markdown --standalone --embed-resources --css="$css" \
    -M title="" -M pagetitle="Jeffrey Hannon Jr. — Resume"
  "$html2pdf" "$html" "$out/$pdf" 0.45 0.6
  echo "built $out/$pdf"
}

build automation content/resume/_index.md static/resume
build hpc content/resume-hpc/_index.md static/resume

for md in private/resume-*.md; do
  [ -e "$md" ] || continue
  variant=$(basename "$md" .md)
  build "${variant#resume-}" "$md" private/resumes
done
