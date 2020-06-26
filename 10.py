def text_match(text):
	return len(text) >= 1 and ('a' <= text[0] <= 'z' or 'A' <= text[0] <= 'Z')
		
print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match(" The quick brown fox jumps over the lazy dog."))
