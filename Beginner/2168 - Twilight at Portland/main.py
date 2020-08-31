n = int(input())

matrix = []

for _ in range(n + 1):
	row = list(map(int, input().split(' ')))
	matrix.append(row)

out_line = []

for i in range(n):
	block_s_or_u = ""

	for j in range(n):
		block = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
		
		if sum(block) >= 2:
			block_s_or_u += "S"
		else:
			block_s_or_u += "U"

	out_line.append(block_s_or_u)

for i in range(n):
	print(out_line[i])