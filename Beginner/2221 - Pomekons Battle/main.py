aux = input()
value = int(aux)

for i in range(value):
	aux = input()
	bonus = int(aux)
	a1, d1, l1 = [int(x) for x in input().split()]
	a2, d2, l2 = [int(x) for x in input().split()]

	valorGolpe1 = (a1 + d1) / 2.0
	if l1 % 2 == 0:
		valorGolpe1 += bonus

	valorGolpe2 = (a2 + d2) / 2.0
	if l2 % 2 == 0:
		valorGolpe2 += bonus

	if valorGolpe1 > valorGolpe2:
		print("Dabriel")
	elif valorGolpe2 > valorGolpe1:
		print("Guarte")
	else:
		print("Empate")