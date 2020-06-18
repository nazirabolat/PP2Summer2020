def isAnagram(s, t):
	return sorted(s) == sorted(t)

s, t = input(), input()
if isAnagram(s, t):
	print("Yes")
else:
	print("No")