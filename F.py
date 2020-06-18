inputline = input().split()
a, b = int(inputline[0]), int(inputline[1])

arr = [[1 for _ in range(b)] for _ in range(a)]

for i in range(1, a):
	for j in range(1, b):
		arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
		
print(arr[-1][-1])