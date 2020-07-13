n_cases = int(input())

solutions = []
solutions.append(0)

for i in range(1, 32):
	solutions.append((2**i) - 1)

for i in range(n_cases):
	value = int(input())

	print(solutions[value])
