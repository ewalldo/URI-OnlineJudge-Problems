n_cases = int(input())

for i in range(n_cases):
	str_input = input()
	half_point = int(len(str_input) / 2)

	first_half = str_input[:half_point]
	second_half = str_input[half_point:]
	first_half = first_half[::-1]
	second_half = second_half[::-1]

	print(first_half + second_half)