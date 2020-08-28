def mdc(a, b):
	if a % b == 0:
		return b
	else:
		return mdc(b, a % b)

n_cases = int(input())

for _ in range(n_cases):
	a, b = map(int, input().split(' '))

	result = mdc(a, b)

	print(result)