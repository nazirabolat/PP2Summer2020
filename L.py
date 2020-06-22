def isBacktoHome(comands):
	x, y = 0, 0
	for comand in comands:
		if comand == 'U':
			x += 1
		elif comand == 'D':
			x -= 1
		elif comand == 'L':
			y += 1
		elif comand == 'R':
			y -= 1
	return x == y == 0

if isBacktoHome(input()):
	print("True")
else:
	print("False")