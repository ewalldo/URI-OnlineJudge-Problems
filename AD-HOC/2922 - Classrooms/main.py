while True:
	try:
		b, u = map(int, input().split(' '))

		if u > b:
			print(u - b - 1)
		elif b > u:
			print(b - u - 1)
		else:
			print(0)
	except EOFError:
		break
