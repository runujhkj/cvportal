.PHONY: resumes serve scan facts forgejo-check

HTML2PDF := build/html2pdf

$(HTML2PDF): scripts/html2pdf.swift
	mkdir -p build && swiftc -O $< -o $@

# Every resume, public and private, through one renderer. See scripts/build_resumes.sh.
resumes: $(HTML2PDF)
	scripts/build_resumes.sh $(HTML2PDF)

serve:
	hugo server --port 1313

scan:
	python3 scripts/scan_projects.py

facts:
	python3 scripts/collect_facts.py

forgejo-check:
	python3 scripts/forgejo.py
