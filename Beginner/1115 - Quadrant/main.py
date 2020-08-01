while True:
	aux = input()
	name = str(aux)
	line = name.strip().split(' ')
	x1 = int(line[0])
	x2 = int(line[1])
	if x1 > 0 and x2 > 0:
		print("primeiro")
	elif x1 < 0 and x2 > 0:
		print("segundo")
	elif x1 < 0 and x2 < 0:
		print("terceiro")
	elif x1 > 0 and x2 < 0:
		print("quarto")
	else:
		break
