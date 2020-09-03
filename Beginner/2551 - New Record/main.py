while True:
	try:
		aux = input()
		days = int(aux)

		record = -1
		for i in range(days):
			t, d = [int(x) for x in input().split()]
			vel = d / t
			if vel > record:
				print(i + 1)
				record = vel
	except EOFError:
		break