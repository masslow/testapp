file = open('5', 'w')
x = 1775
for e in range(109):
	x = x+25
	input = str(x) + ' ' +  str(raw_input(x)) + '\n'
	file.write(input)
1
file.close 