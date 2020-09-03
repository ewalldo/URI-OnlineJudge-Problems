while True:
	try:
		aux = input()
		size = int(aux)

		up = 0
		down = 0
		for i in range(size):
			n, c = [int(x) for x in input().split()]
			up += (c * n)
			down += c
		down *= 100
		print("%.4f" % (up / down))
	except EOFError:
		break