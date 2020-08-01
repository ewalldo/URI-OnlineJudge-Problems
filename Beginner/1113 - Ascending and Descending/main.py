while True:
	aux = input()
	name = str(aux)
	line = name.strip().split(' ')
	x1 = int(line[0])
	x2 = int(line[1])

	if x1 == x2:
		break

	if x1 > x2:
		print("Decrescente")
	else:
		print("Crescente")
