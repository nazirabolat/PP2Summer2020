def text_match(text):
	return len(text) >= 1 and ('a' <= text[-1] <= 'z' or 'A' <= text[-1] <= 'Z' or text[-1] in ['.', ',', '!', '?'])
		
print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("The quick brown fox jumps over the lazy dog. "))
print(text_match("The quick brown fox jumps over the lazy dog "))