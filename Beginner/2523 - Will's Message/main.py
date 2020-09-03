while True:
	try:
		aux = input()
		name = str(aux)

		aux = input()
		size = int(aux)

		aux = input()
		line = str(aux)
		line = line.strip().split()

		for i in range(size):
			print("%c" % (name[int(line[i]) - 1]), end='')
		print("")

	except EOFError:
		break