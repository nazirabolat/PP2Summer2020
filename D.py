n = int(input())

tribonachi = [0, 1, 1]
for i in range(n - 2):
	tribonachi.append(tribonachi[-1] + tribonachi[-2] + tribonachi[-3])
if n == 0:
	print(0)
else:
	print(tribonachi[-1])