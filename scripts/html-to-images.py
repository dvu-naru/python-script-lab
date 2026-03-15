from html2image import Html2Image

file = str(input('Enter the directory of your html file: '))
img = str(input('Enter the name of your image including file format: '))
backgroud = str(input('Enter backgroud: '))

hti = Html2Image(browser_executable='/usr/bin/chromium-browser')


if (len(backgroud) > 0):
	css = ('body {backgroud: %s;}' % (backgroud))
	with open(file, errors='ignore') as f:
		hti.screenshot(f.read, css_str=css, save_img=img)
else:
	with open(file, errors='ignore') as f:
		hti.screenshot(f.read, save_img=img)