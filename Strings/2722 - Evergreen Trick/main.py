n_cases = int(input())

for _ in range(n_cases):
	str_1 = input()
	str_2 = input()

	size_str_1 = len(str_1)
	size_str_2 = len(str_2)

	out_str = ""
	for i in range(int(size_str_1 / 2) - 1):
		out_str += str_1[i * 2:i * 2 + 2]
		out_str += str_2[i * 2:i * 2 + 2]
	out_str += str_1[-2:]
	if size_str_1 == size_str_2:
		out_str += str_2[-2:]
	else:
		out_str += str_2[-1:]

	print(out_str)