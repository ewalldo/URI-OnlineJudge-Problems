count = 0
soma = 0
while True:
	aux = input()
	line = str(aux)

	if line == "caw caw":
		count += 1
		print(soma)
		soma = 0
		if count >= 3:
			break
	else:
		x1 = line[0]
		x2 = line[1]
		x3 = line[2]

		if x1 == '-':
			v1 = 0
		else:
			v1 = 4
		if x2 == '-':
			v2 = 0
		else:
			v2 = 2
		if x3 == '-':
			v3 = 0
		else:
			v3 = 1

		soma += (v1 + v2 + v3)