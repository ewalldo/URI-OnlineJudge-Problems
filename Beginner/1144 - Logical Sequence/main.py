aux = input()
value = int(aux)

for i in range(1, value + 1):
	print("%d %d %d" % (i, i * i, i * i * i))
	print("%d %d %d" % (i, i * i + 1, i * i * i + 1))
