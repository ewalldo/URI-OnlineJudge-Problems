while True:
	try:
		input_str = input()

		next_case = 1 #1 = uppercase, 0 = lowercase
		out_str = ""

		for i in range(len(input_str)):
			if input_str[i] == ' ':
				out_str += ' '
			else:
				if next_case == 1:
					out_str += input_str[i].upper()
					next_case = 0
				else:
					out_str += input_str[i].lower()
					next_case = 1

		print(out_str)
	except EOFError:
		break