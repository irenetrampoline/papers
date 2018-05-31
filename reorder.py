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
g.close()