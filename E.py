stack = []

while True:
	line = input().split()

	if line[0] == 'push':
		stack.append(int(line[1]))
		print("OK")
	elif line[0] == 'size':
		print(len(stack))
	elif line[0] == 'back':
		print(stack[-1])
	elif line[0] == 'front':
		print(stack[0])
	elif line[0] == 'pop':
		stack.pop()
		print("OK")
	elif line[0] == 'clear':
		stack = []
		print("OK")
	else:
		print("Black Devil")
		break