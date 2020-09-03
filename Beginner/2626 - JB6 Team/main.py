while True:
	try:
		aux = input()
		name = str(aux)
		line = name.strip().split()
		x1 = line[0]
		x2 = line[1]
		x3 = line[2]

		if (x1 == "papel" and x2 == "pedra" and x3 == "pedra") or (x1 == "pedra" and x2 == "tesoura" and x3 == "tesoura") or (x1 == "tesoura" and x2 == "papel" and x3 == "papel"):
			print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
		elif (x2 == "papel" and x1 == "pedra" and x3 == "pedra") or (x2 == "pedra" and x1 == "tesoura" and x3 == "tesoura") or (x2 == "tesoura" and x1 == "papel" and x3 == "papel"):
			print("Iron Maiden's gonna get you, no matter how far!")
		elif (x3 == "papel" and x2 == "pedra" and x1 == "pedra") or (x3 == "pedra" and x2 == "tesoura" and x1 == "tesoura") or (x3 == "tesoura" and x2 == "papel" and x1 == "papel"):
			print("Urano perdeu algo muito precioso...")
		else:
			print("Putz vei, o Leo ta demorando muito pra jogar...")
	except EOFError:
		break