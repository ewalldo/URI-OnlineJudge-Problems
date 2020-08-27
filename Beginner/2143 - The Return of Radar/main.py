while True:
	aux = input()
	value = int(aux)

	if value == 0:
		break

	for i in range(value):
		aux = input()
		n_people = int(aux)

		if n_people % 2 == 0:
			print((n_people - 2) * 2 + 2)
		else:
			print((n_people - 1) * 2 + 1)