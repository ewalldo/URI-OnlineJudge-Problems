while True:
	aux = input()
	value = int(aux)

	if value == 0:
		break

	for i in range(1, value + 1):
		if i != value:
			print("%d " % (i), end='')
		else:
			print("%d" % (i))
