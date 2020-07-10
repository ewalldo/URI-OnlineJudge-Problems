while True:
	try:
		n_cases = int(input())
		id_list = []

		for i in range(n_cases):
			id_list.append(input())

		id_list = sorted(id_list)
		for i in range(n_cases):
			print(id_list[i])
	except EOFError:
		break
