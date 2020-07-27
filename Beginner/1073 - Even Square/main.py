aux = input()
name = int(aux)
for i in range(2, name + 1, 2):
	if i % 2 == 0:
		power = i * i
		print("%d^2 = %d" % (i, power))
