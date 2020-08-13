aux = input()
name = int(aux)
value = 0
for i in range(1000):
	print("N[%d] = %d" % (i, value))
	value += 1
	if value >= name:
		value = 0