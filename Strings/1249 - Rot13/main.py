while True:
	try:
		input_str = input()
		out_str = ""

		for char in input_str:
			if char.isalpha():
				char_ = ord(char) + 13
				if char.isupper():
					if char_ > 90:
						char_ -= 26
					out_str += chr(char_)
				else:
					if char_ > 122:
						char_ -= 26
					out_str += chr(char_)
			else:
				out_str += char
		print(out_str)
	except EOFError:
		break