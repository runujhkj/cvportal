resume:
	cd static/resume && pandoc ../../resume.md -o jack-resume.html --css=resume.css --standalone --from markdown

resume-hpc:
	cd static/resume && pandoc ../../resume-hpc.md -o jack-resume-hpc.pdf --standalone --from markdown -V geometry:margin=0.75in -V fontsize=10pt -M title=""

serve:
	hugo server --port 1313

scan:
	python3 scripts/scan_projects.py
