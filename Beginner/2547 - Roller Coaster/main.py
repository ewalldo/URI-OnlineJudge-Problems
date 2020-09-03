while True:
	try:
		n, amin, amax = [int(x) for x in input().split()]

		count = 0
		for i in range(n):
			aux = input()
			height = int(aux)

			if height >= amin and height <= amax:
				count += 1

		print(count)
	except EOFError:
		break