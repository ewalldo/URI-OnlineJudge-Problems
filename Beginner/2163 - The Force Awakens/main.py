n, m = [int(x) for x in input().split()]

list_42 = []
matrix = [[0 for x in range(m)] for y in range(n)]
for i in range(n):
	value = str(input())
	values = value.split()
	for j in range(m):
		matrix[i][j] = int(values[j])
		if matrix[i][j] == 42:
			list_42.append([i, j])

x_out = 0
y_out = 0
for i in range(len(list_42)):
	x, y = list_42[i][0], list_42[i][1]

	if x == 0 or x == n - 1 or y == 0 or y == m - 1:
		continue
	else:
		if (matrix[x - 1][y - 1] == 7) and (matrix[x][y - 1] == 7) and (matrix[x + 1][y - 1] == 7) and (matrix[x - 1][y] == 7) and (matrix[x + 1][y] == 7) and (matrix[x - 1][y + 1] == 7) and (matrix[x][y + 1] == 7) and (matrix[x + 1][y + 1] == 7):
			x_out = x + 1
			y_out = y + 1
			break
print("%d %d" %(x_out, y_out))