n_p = 0
soma = 0
while True:
	aux = input()
	value = int(aux)

	if value < 0:
		break

	soma += value
	n_p += 1
print("%.2f" % (soma / n_p))
