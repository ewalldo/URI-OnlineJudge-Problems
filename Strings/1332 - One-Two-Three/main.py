n_cases = int(input())

for i in range(n_cases):
	input_str = input()

	if len(input_str) != 3:
		print(3)
	else:
		if (input_str[0] == 'o' and input_str[1] == 'n') or (input_str[0] == 'o' and input_str[2] == 'e') or (input_str[1] == 'n' and input_str[2] == 'e'):
			print(1)
		else:
			print(2)
