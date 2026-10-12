.PHONY: resume resume-hpc serve scan facts forgejo-check

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
