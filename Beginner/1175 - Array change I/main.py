x = [0] * 20

for i in range(20):
	aux = input()
	name = int(aux)
	x[19 - i] = name

for i in range(20):
	print("N[%d] = %d" % (i, x[i]))