while True:
	try:
		n, q = [int(x) for x in input().split()]
		x = []
		for i in range(n):
			aux = input()
			value = int(aux)
			x.append(value)
		x = sorted(x)
		for i in range(q):
			aux = input()
			value = int(aux)
			print(x[n - value])
	except EOFError:
		break