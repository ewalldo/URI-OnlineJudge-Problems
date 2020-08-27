while True:
	try:
		input_str = input().lower()
		input_str = input_str.split('-')

		if (input_str[0][0] == 'c' or input_str[0][-1] == 'c') and (input_str[1][0] == 'o' or input_str[1][-1] == 'o') and (input_str[2][0] == 'b' or input_str[2][-1] == 'b') and (input_str[3][0] == 'o' or input_str[3][-1] == 'o') and (input_str[4][0] == 'l' or input_str[4][-1] == 'l'):
			print("GRACE HOPPER")
		else:
			print("BUG")
	except EOFError:
		break