input_line = input().split()
days, h = int(input_line[0]), int(input_line[1])
valid = False

for i in range(days):
	average = sum([int(x) for x in input().split()]) / 3
	if average >= h:
		valid = True
		break

if valid:
	print("YES")
else:
	print("NO")