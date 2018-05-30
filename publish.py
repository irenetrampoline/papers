import argparse
import time
import py.test
import re
import shutil
import os
import urllib2
from os.path import join

PDF_DIR = 'pdfs/'
WRITEUP_DIR = 'writeups/'

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", required = False, default="writeups/today.md",help="writeup filename")
	parser.add_argument("--date",required = False, help="date in MM-DD-YYYY, today if not provided")
	# parser.add_argument("--outfile",required = True,  help="directory and file name you wish to store the cleaned up output in")
	args = parser.parse_args()

	f = open(args.input, 'rb')
	writeup = f.readlines()
	f.close()

	info_line = writeup[2]

	if 'Author 1' in info_line:
		raise ValueError('today.md has no new information.')

	authors_raw = info_line.split('[')[0]
	authors_lst = authors_raw.split(', ')
	authors_N = len(authors_lst)
	try:
		all_nums = re.findall(r'\d+', writeup[2])

		year = all_nums[-1]
	except:
		raise ValueError('Year must end with e.g. "2014."')

	if authors_N < 4: 
		md_title = []
		for a in authors_lst:
			a = a.strip()
			first3 = a.split(' ')[-1][:3].replace('.', '')
			md_title.append(first3)
		md_title = ''.join(md_title)
	else:
		a = authors_lst[0]
		first3 = a.split(' ')[-1][:3].replace('.', '')
		md_title = '%sEtAl' % first3

	md_title = md_title + str(year)[-2:]
	md_fname = join(WRITEUP_DIR, md_title + '.md')

	g = open(md_fname, 'wb')
	g.writelines(writeup)
	g.close()

	print 'Wrote file to %s' % md_fname

	title = re.findall('\[(.*?)\]', info_line)[0]
	url = re.findall('\((.*?)\)', info_line)[0]

	f = open('README.md', 'rb')
	readme = f.readlines()
	f.close()

	g = open('README_new.md', 'wb')
	# readme = ['**MORE TO COME!**']
	# py.test.set_trace()
	for line in readme:
		if '**MORE TO COME!**' in line:
			date = time.strftime("%b %d, %Y")
			authors_lst_short = list()
			for a in authors_lst:
				names = a.split(' ')
				first = names[0]
				# py.test.set_trace()
				short_name = '%s. %s' % (first[0], ' '.join(names[1:]))
				authors_lst_short.append(short_name)
			authors_short = ', '.join(authors_lst_short)
			new_line = '**%s:** [%s](%s) %s%s. [[pdf]](%s)' % (
				date, title, md_fname, authors_short, str(year), url
				)
			g.write(new_line + '\n')
			g.write('\n')
		g.write(line)
	g.close()

	shutil.copy('README.md', 'README_old.md')
	shutil.move('README_new.md', 'README.md')

	shutil.copy('writeups/today.md', 'writeups/old.md')
	shutil.copy('writeups/template.md', 'writeups/today.md')

	pdf_fname = join(PDF_DIR, md_title + '.pdf')
	try:
		download_file(url, pdf_fname)
	except:
		print 'Failed to download: %s' % url
	print 'Updated README.md'
	print 'Downloaded PDF file in %s' % pdf_fname
	# print title
	# print url

	# rename today.md (md title)
	# Add info to readme (authors, title, md title, URL, date)

def download_file(download_url, fname):
    response = urllib2.urlopen(download_url)
    file = open("%s.pdf" % fname, 'wb')
    file.write(response.read())
    file.close()
    print("Completed")

if __name__ == '__main__':
	main()