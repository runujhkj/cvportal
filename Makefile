resume:
	cd static/resume && pandoc ../../resume.md -o jack-resume.html --css=resume.css --standalone --from markdown
