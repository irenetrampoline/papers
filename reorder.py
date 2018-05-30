f = open('README.md', 'rb')
readme = f.readlines()
f.close()

g = open('README_new.md', 'wb')

before = list()
is_before = True
after = list()

for line in readme:
	if '**MORE TO COME!**' in line:
		is_before = False
	if is_before:
		before.append(line)
	else:
		after.append(line)

for line in before[::-1]:
	g.write(line)

for line in after:
	g.write(line)
	
	# 	date = time.strftime("%b %d, %Y")
	# 	authors_lst_short = list()
	# 	for a in authors_lst:
	# 		names = a.split(' ')
	# 		first = names[0]
	# 		# py.test.set_trace()
	# 		short_name = '%s. %s' % (first[0], ' '.join(names[1:]))
	# 		authors_lst_short.append(short_name)
	# 	authors_short = ', '.join(authors_lst_short)
	# 	new_line = '**%s:** [%s](%s) %s%s. [[pdf]](%s)' % (
	# 		date, title, md_fname, authors_short, str(year), url
	# 		)
	# 	g.write(new_line + '\n')
	# 	g.write('\n')
	# g.write(line)
g.close()