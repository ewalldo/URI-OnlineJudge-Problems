while True:
	try:
		n, i = [int(x) for x in input().split()]

		count = 0
		for j in range(n):
			q, w = [int(x) for x in input().split()]
			if q == i and w == 0:
				count += 1
		print(count)
	except EOFError:
		break