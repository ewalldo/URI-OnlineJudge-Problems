while True:
	try:
		value = int(input())
		min_v = int(value / 3)
		max_v = value - min_v
		center = int(value / 2.0)

		matrix = [[0 for x in range(value)] for y in range(value)]
		for i in range(value):
			for j in range(value):
				if i == j:
					matrix[i][j] = 2
				if i + j == value - 1:
					matrix[i][j] = 3
				if i >= min_v and i < max_v and j >= min_v and j < max_v:
					matrix[i][j] = 1

		matrix[center][center] = 4
		for i in range(value):
			for j in range(value):
				print(matrix[i][j], end="")
			print("")
		print("")
	except EOFError:
		break