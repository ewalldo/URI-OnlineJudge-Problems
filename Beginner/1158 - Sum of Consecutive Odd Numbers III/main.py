aux = input()
name = int(aux)
for i in range(name):
	aux = input()
	line = str(aux)
	line = line.strip().split(' ')
	x1 = int(line[0])
	x2 = int(line[1])

	soma = 0
	for j in range(x2):
		if x1 % 2 == 1:
			soma += x1
			x1 += 2
		else:
			x1 += 1
			soma += x1
			x1 += 2
	print(soma)
