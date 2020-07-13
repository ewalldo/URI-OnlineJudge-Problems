n_cases = int(input())

for i in range(n_cases):
	final_output = ""

	a, b = map(int, input().split(' '))

	for j in range(a, b+1):
		final_output += str(j)

	final_output += (final_output[::-1])

	print(final_output)
