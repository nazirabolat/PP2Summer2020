def text_match(text):
	for sequence in text.split('_'):
		for ch in sequence:
			if not 'a' <= ch <= 'z':
				return False
	return True

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))