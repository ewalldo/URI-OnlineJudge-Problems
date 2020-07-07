num_input = int(input())

for i in range(num_input):
	str_1, str_2 = input().split(' ')

	size_1 = len(str_1)
	size_2 = len(str_2)

	output = ""
	for i in range(min(size_1, size_2)):
		output = output + str_1[i] + str_2[i]

	if size_1 > size_2:
		output = output + str_1[size_2:]
	elif size_2 > size_1:
		output = output + str_2[size_1:]

	print(output)
