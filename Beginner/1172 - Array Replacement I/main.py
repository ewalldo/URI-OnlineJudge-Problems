for i in range(10):
	aux = input()
	name = int(aux)

	if name <= 0:
		print("X[%d] = 1" %(i))
	else:
		print("X[%d] = %d" %(i, name))
