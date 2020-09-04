first_case = True

while True:
	n_cases = int(input())

	if n_cases == 0:
		break

	names = []
	size = []

	for _ in range(n_cases):
		input_str = input()
		names.append(input_str)
		size.append(len(input_str))

	if not first_case:
		print("")

	for name in names:
		print(name.rjust(max(size)))
		first_case = False