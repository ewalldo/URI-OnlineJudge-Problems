aux = input()
name = int(aux)

for i in range(name):
	aux = input()
	x1 = str(aux)
	aux = input()
	x2 = str(aux)

	if x1 == "ataque" and x2 == "pedra":
		print("Jogador 1 venceu")
	elif x2 == "ataque" and x1 == "pedra":
		print("Jogador 2 venceu")
	elif x1 == "pedra" and x2 == "papel":
		print("Jogador 1 venceu")
	elif x2 == "pedra" and x1 == "papel":
		print("Jogador 2 venceu")
	elif x1 == "ataque" and x2 == "papel":
		print("Jogador 1 venceu")
	elif x1 == "papel" and x2 == "ataque":
		print("Jogador 2 venceu")
	elif x1 == "papel" and x2 == "papel":
		print("Ambos venceram")
	elif x1 == "pedra" and x2 == "pedra":
		print("Sem ganhador")
	elif x1 == "ataque" and x2 == "ataque":
		print("Aniquilacao mutua")