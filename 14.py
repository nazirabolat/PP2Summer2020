def text_match(text):
	for ch in text:
		if not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9' or ch == '_'):
			return False
	return True
		
print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))