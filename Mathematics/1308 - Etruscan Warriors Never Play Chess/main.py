import math

n_cases = int(input())

for _ in range(n_cases):
	n_warriors = int(input())

	n_rows = int(math.sqrt((2 * n_warriors) + 0.25) - 0.5)
	print(n_rows)