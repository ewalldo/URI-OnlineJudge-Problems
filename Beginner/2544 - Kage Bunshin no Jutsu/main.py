while True:
	try:
		aux = input()
		value = int(aux)

		count = 0
		while value != 0:
			value = int(value / 2)
			count += 1
		print(count - 1)
	except EOFError:
		break