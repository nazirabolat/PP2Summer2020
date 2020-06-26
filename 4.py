def text_match(text):
	return text != '' and text[0] == 'a'
		
print(text_match("ac"))
print(text_match("abc"))
print(text_match("b"))