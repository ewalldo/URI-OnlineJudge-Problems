def generateMatrix(num):
	matrix = [[num for x in range(num)] for y in range(num)] 

	value = 1
	for i in range(num):
		for j in range(i, num - i):
			matrix[i][j] = value
			matrix[j][i] = value
			matrix[(num-1) - i][j] = value
			matrix[j][(num-1) - i] = value
		value += 1

	return matrix

while True:
	aux = input()
	if (int(aux) == 0.00):
		break
	else:
		size = int(aux)
		mat = generateMatrix(int(aux))
		for i in range(size):
			for j in range(size):
				if j == 0:
					print("{:>3}".format(mat[i][j]), end='')
				else:
					print("{:>4}".format(mat[i][j]), end='')
			print("")
		print("")