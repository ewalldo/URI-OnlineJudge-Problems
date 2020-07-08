n_cases = int(input())

for i in range(n_cases):
	height, diameter, branches = map(int, input().split(' '))

	if height >= 200 and height <= 300 and diameter >= 50 and branches >= 150:
		print("Sim")
	else:
		print("Nao")
