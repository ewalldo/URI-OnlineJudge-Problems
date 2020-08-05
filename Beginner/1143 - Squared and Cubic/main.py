aux = input()
num = int(aux)

for i in range(1, num + 1):
	print("%d " % (i), end='')
	print("%d " % (i * i), end='')
	print("%d" % (i * i * i))
