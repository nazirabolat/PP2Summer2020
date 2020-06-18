input_line = input().split()
l, r = int(input_line[0]), int(input_line[1])
bad_nums = []
for i in range(l, r + 1):
	if i % 7 == 1 or i % 7 == 2 or i % 7 == 5:
		bad_nums.append(str(i))
ans = (' '.join(bad_nums))
if ans != '':
	print(ans + ' ')
else:
	print('')