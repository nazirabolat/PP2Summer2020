def text_match(text):
	return len(text) >= 2 and text[0] == 'a' and text[1] =='b' 
		
print(text_match("ac"))
print(text_match("abc"))
print(text_match("b"))