while True:
	try:
		aux = input()
		name = int(aux)
		aux = input()
		values = str(aux)
		values = values.strip().split()
		maior = -1

		flag = 0
		for i in range(len(values)):
			if int(values[i]) > maior:
				maior = int(values[i])
				if maior >= 20:
					print("3")
					flag = 1
					break

		if flag == 1:
			continue
		else:
			if maior >= 10:
				print("2")
			else:
				print("1")
	except EOFError:
		break