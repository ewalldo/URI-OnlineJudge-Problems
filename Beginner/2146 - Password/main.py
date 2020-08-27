while True:
	try:
		aux = input()
		name = int(aux)
		print(name - 1)
	except EOFError:
		break