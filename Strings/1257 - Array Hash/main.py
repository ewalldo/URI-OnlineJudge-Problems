n_cases = int(input())

for i in range(n_cases):
	n_strings = int(input())
	sum_code = 0

	for j in range(n_strings):
		string_code = input()

		for k in range(len(string_code)):
			sum_code += ((ord(string_code[k]) - 65) + j + k)

	print(sum_code)
