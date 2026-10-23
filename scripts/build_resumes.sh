#!/usr/bin/env bash
# Builds every resume to PDF with one renderer: pandoc to standalone HTML, then the
# system WebKit (scripts/html2pdf.swift) to US Letter PDF.
# Public variants come from content/ and land in static/resume/, where the site links
# to them. Private variants come from the gitignored private/ folder and stay there.
set -euo pipefail
cd "$(dirname "$0")/.."
html2pdf=${1:-build/html2pdf}
css=static/resume/resume.css
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

build() {  # variant source output-dir
  local html="$tmp/$1.html"
  pandoc "$2" -o "$html" --from markdown --standalone --embed-resources --css="$css" \
    -M title="" -M pagetitle="Jeffrey Hannon Jr. — Resume"
  "$html2pdf" "$html" "$3/resume-$1.pdf" 0.45 0.6
  echo "built $3/resume-$1.pdf"
}

build automation content/resume/_index.md static/resume
build hpc content/resume-hpc/_index.md static/resume

for md in private/resume-*.md; do
  [ -e "$md" ] || continue
  variant=$(basename "$md" .md)
  build "${variant#resume-}" "$md" private
done
