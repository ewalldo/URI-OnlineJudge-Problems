num_input = int(input())

for i in range(num_input):
	str_input = input().split(' ')

	output = ""

	for i in range(len(str_input)):
		if len(str_input[i]) > 0:
			output = output + str_input[i][0]

	print(output)
