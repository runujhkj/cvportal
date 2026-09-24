CHROME ?= /Applications/Google Chrome.app/Contents/MacOS/Google Chrome

resume:
	cd static/resume && pandoc ../../resume.md -o jack-resume.html --css=resume.css --standalone --from markdown -M title="" -M pagetitle="Jeffrey Hannon Jr. — Resume"
	"$(CHROME)" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="$(CURDIR)/static/resume/jack-resume.pdf" "file://$(CURDIR)/static/resume/jack-resume.html" 2>/dev/null

resume-hpc:
	cd static/resume && pandoc ../../resume-hpc.md -o jack-resume-hpc.pdf --standalone --from markdown -V geometry:margin=0.75in -V fontsize=10pt -M title=""

serve:
	hugo server --port 1313

scan:
	python3 scripts/scan_projects.py
