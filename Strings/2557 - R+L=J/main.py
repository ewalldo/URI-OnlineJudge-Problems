while True:
	try:
		input_str = input()

		r = input_str.split('+')[0]
		l = input_str.split('=')[0].split("+")[1]
		j = input_str.split('=')[1]

		if r == "R":
			print(int(j) - int(l))
		elif l == "L":
			print(int(j) - int(r))
		elif j == "J":
			print(int(r) + int(l))
	except EOFError:
		break
