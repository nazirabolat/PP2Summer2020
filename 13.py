def text_match(text):
	return 'z' in text and len(text) >= 1 and text[0] != 'z' and text[-1] != 'z' 
		
print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python Exercises."))