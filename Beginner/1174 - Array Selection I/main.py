for i in range(100):
	aux = input()
	name = float(aux)
	if name <= 10.0:
		print("A[%d] = %.1f" % (i, name))