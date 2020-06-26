def text_match(text):
	return len(text) >= 3 and text[:4] == 'abb'
		
print(text_match("ac"))
print(text_match("abc"))
print(text_match("b"))