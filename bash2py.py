import os
import sys
import subprocess

def translate(bash_filename, html):
	subprocess.run(['bash-4.3.30/bash2pyengine', html, bash_filename])

def helpx():
	print('Usage:\n./bash2py [-h] [-d] <dir_name>\n./bash2py [-h] [-f] <file_name>\n  -h: generate html diff not python code')

def main():

	html   = ''
	option = ''

	lth = len(sys.argv)

	if lth == 1:
		helpx()
		exit(0)

	bash_filename = sys.argv[-1]
	for i in range(1, lth - 1) :
		if sys.argv[i] == '-f' or sys.argv[i] == '-d':
			option = sys.argv[i]
		elif sys.argv[i] == '-h':
			html   = '--html'

	if option == '':
		if os.path.isdir(bash_filename):
			option = '-d'
		elif os.path.isfile(bash_filename):
			option = '-f'

	if option == '-f':
		translate(bash_filename, html)
		exit(0)

	if option == '-d':
		for dirname, sub_dirs, files in os.walk(bash_filename):
			for f in files:
				if not f.endswith('.py') and not f.endswith('.html'):
					bash_filename1 = os.path.join(dirname, f)
					translate(bash_filename1, html)
		exit(0)

if __name__ == '__main__':
	main()
