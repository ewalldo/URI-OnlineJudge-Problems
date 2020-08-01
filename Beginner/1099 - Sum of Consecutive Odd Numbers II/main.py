aux = input()
name = int(aux)
for i in range(name):
	soma = 0
	aux = input()
	data = str(aux)
	line = data.strip().split(' ')
	x1 = int(line[0])
	x2 = int(line[1])

	if x1 == x2:
		print(0)
		continue

	if (x2 < x1):
		temp = x2
		x2 = x1
		x1 = temp

	for j in range(x1 + 1, x2):
		if j % 2 != 0:
			soma += j
	print(soma)
