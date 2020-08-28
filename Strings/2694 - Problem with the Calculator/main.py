n_cases = int(input())

for _ in range(n_cases):
	input_str = input()
	out_str = ""

	for i in input_str:
		if i.isdigit():
			out_str += i
		else:
			out_str += '*'

	out_str = out_str.split('*')
	total = 0
	for value in out_str:
		if value != '':
			total += int(value)

	print(total)