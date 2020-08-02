aux = input()
name = int(aux)

for i in range(name):
	aux = input()
	name = str(aux)
	line = name.strip().split(' ')
	x1 = int(line[0])
	x2 = int(line[1])
	if x2 == 0:
		print("divisao impossivel")
	else:
		print("%.1f" % (x1 / x2))
