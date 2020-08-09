while True:
	aux = input()
	name = int(aux)

	if name == 0:
		break

	soma = 0
	for i in range(5):
		if name % 2 == 0:
			soma += name
			name += 2
		else:
			name += 1
			soma += name
			name += 2
	print(soma)
