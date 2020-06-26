def text_match(text):
	return len(text) >= 4 and text[:4] == 'abbb'
		
print(text_match("ac"))
print(text_match("abc"))
print(text_match("b"))