n_cases = int(input())

for _ in range(n_cases):
	x, y = map(int, input().split('x'))

	for i in range(5, 11):
		if x == y:
			print(str(x) + " x " + str(i) + " = " + str(x * i))
		else:
			print(str(x) + " x " + str(i) + " = " + str(x * i) + " && " + str(y) + " x " + str(i) + " = " + str(y * i))