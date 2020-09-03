while True:
	try:
		v1, v2 = [int(x) for x in input().split()]

		matrix = [[0 for x in range(v2)] for y in range(v1)]
		for i in range(v1):
			value = str(input())
			values = value.split()
			for j in range(len(values)):
				if values[j] == "1":
					matrix[i][j] = 9
					if j + 1 < v2 and matrix[i][j+1] != 9:
						matrix[i][j+1] += 1
					if i + 1 < v1 and matrix[i+1][j] != 9:
						matrix[i+1][j] += 1
					if j - 1 >= 0 and matrix[i][j-1] != 9:
						matrix[i][j-1] += 1
					if i - 1 >= 0 and matrix[i-1][j] != 9:
						matrix[i-1][j] += 1

		for i in range(v1):
			for j in range(v2):
				print(matrix[i][j], end="")
			print("")
	except EOFError:
		break