#!/usr/bin/env bash
# Builds every resume to PDF with one renderer: contact placeholders filled from
# data/contact.toml, pandoc to standalone HTML, then the system WebKit
# (scripts/html2pdf.swift) to US Letter PDF.
#
# Normal build: public variants come from content/ and land in static/resume/, where
# the site links to them; private variants come from the gitignored private/ folder
# and stay there. No postal address is ever included.
#
# --share: every variant, public and private, is built with the postal address from
# private/contact.toml into private/share/ (gitignored), for sending to one person.
set -euo pipefail
cd "$(dirname "$0")/.."
html2pdf=${1:-build/html2pdf}
mode=${2:-}
css=static/resume/resume.css
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

address_flag=""
if [ "$mode" = "--share" ]; then
  address_flag="--with-address"
  mkdir -p private/share
fi

build() {  # variant source output-dir
  local md="$tmp/$1.md" html="$tmp/$1.html" out="$3"
  [ -n "$address_flag" ] && out=private/share
  python3 scripts/expand_contact.py "$2" $address_flag > "$md"
  pandoc "$md" -o "$html" --from markdown --standalone --embed-resources --css="$css" \
    -M title="" -M pagetitle="Jeffrey Hannon Jr. — Resume"
  "$html2pdf" "$html" "$out/resume-$1.pdf" 0.45 0.6
  echo "built $out/resume-$1.pdf"
}

build automation content/resume/_index.md static/resume
build hpc content/resume-hpc/_index.md static/resume

for md in private/resume-*.md; do
  [ -e "$md" ] || continue
  variant=$(basename "$md" .md)
  build "${variant#resume-}" "$md" private
done
