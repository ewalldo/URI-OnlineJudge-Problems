while True:
	try:
		aux = input()
		size = int(aux)
		aux = input()
		line = str(aux)

		line = line.strip().split()

		inp = (size * 2) / 3
		count = 0
		for i in range(size):
			if int(line[i]) == 1:
				count += 1
			if count >= inp:
				break
		if count >= inp:
			print("impeachment")
		else:
			print("acusacao arquivada")
	except EOFError:
		break