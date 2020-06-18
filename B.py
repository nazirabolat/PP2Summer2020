letters = input()
ans = []
for aski in range(26):
    ch = chr(aski + ord('a'))
    for letter in letters:
        if ch == letter:
            ans.append(ch)
print(''.join(ans))
