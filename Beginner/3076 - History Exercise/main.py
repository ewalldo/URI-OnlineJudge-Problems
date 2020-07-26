while True:
	try:
		year_value = int(input())

		if year_value % 100 == 0:
			print(year_value // 100)
		else:
			print(year_value // 100 + 1)
	except EOFError:
		break
