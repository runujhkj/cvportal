resume:
	cd static/resume && pandoc ../../resume.md -o jack-resume.html --css=resume.css --standalone --from markdown

resume-hpc:
	cd static/resume && pandoc ../../resume-hpc.md -o jack-resume-hpc.pdf --css=resume.css --standalone --from markdown -V geometry:margin=0.75in -V fontsize=10pt

serve:
	hugo server --port 1313
