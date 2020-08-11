aux = input()
name = int(aux)
for i in range(name):
	aux = input()
	value = int(aux)

	if value == 1:
		print("1 nao eh perfeito")
		continue

	soma = 1
	for j in range(2, int(value / 2) + 1):
		if value % j == 0:
			soma += j
	if soma == value:
		print("%d eh perfeito" % (value))
	else:
		print("%d nao eh perfeito" % (value))
