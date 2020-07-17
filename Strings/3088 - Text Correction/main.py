while True:
	try:
		input_str = input()
		out_str = ""

		for i in range(len(input_str)):
			if input_str[i] == '.' and input_str[i - 1] == ' ':
				out_str = out_str[:len(out_str) - 1]
				out_str += "."
			elif input_str[i] == ',' and input_str[i - 1] == ' ':
				out_str = out_str[:len(out_str) - 1]
				out_str += ","
			else:
				out_str += input_str[i]

		print(out_str)
	except EOFError:
		break
