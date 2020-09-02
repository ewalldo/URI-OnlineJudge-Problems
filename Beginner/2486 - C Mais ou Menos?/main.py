while True:
	aux = input()
	size = int(aux)

	if size == 0:
		break

	total = 0
	for i in range(size):
		aux = input()
		name = str(aux)
		line = name.strip().split()
		n_i = int(line[0])
		a = ""
		for j in range(1, len(line)):
			a += line[j]
			if j != len(line) - 1:
				a += " "
		#print(a)

		if a == "suco de laranja":
			total += (n_i * 120)
		elif a == "morango fresco":
			total += (n_i * 85)
		elif a == "mamao":
			total += (n_i * 85)
		elif a == "goiaba vermelha":
			total += (n_i * 70)
		elif a == "manga":
			total += (n_i * 56)
		elif a == "laranja":
			total += (n_i * 50)
		elif a == "brocolis":
			total += (n_i * 34)

	if total > 130:
		print("Menos %d mg" % (total - 130))
	elif total < 110:
		print("Mais %d mg" % (110 - total))
	else:
		print("%d mg" % (total))