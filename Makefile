.PHONY: resume resume-hpc private-resumes serve scan facts forgejo-check

resume:
	cd static/resume && pandoc ../../resume.md -o jack-resume.html --css=resume.css --standalone --from markdown -M title="" -M pagetitle="Jeffrey Hannon Jr. — Resume"
	swift scripts/html2pdf.swift static/resume/jack-resume.html static/resume/jack-resume.pdf 0.45 0.6

resume-hpc:
	cd static/resume && pandoc ../../resume-hpc.md -o jack-resume-hpc.pdf --standalone --from markdown -V geometry:margin=0.6in -V fontsize=10pt -M title="" -H ../../pandoc/resume-hpc.tex

serve:
	hugo server --port 1313

scan:
	python3 scripts/scan_projects.py

facts:
	python3 scripts/collect_facts.py

forgejo-check:
	python3 scripts/forgejo.py

# Builds every private/resume-*.md (gitignored, never published) to HTML and PDF beside it.
private-resumes:
	@for md in private/resume-*.md; do \
		[ -e "$$md" ] || { echo "no private/resume-*.md files"; exit 1; }; \
		base=$${md%.md}; \
		pandoc "$$md" -o "$$base.html" --css=static/resume/resume.css --embed-resources --standalone --from markdown -M title="" -M pagetitle="Jeffrey Hannon Jr. — Resume" && \
		swift scripts/html2pdf.swift "$$base.html" "$$base.pdf" 0.45 0.6 && echo "built $$base.pdf"; \
	done
