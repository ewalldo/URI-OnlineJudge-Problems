n_cases = int(input())

for i in range(n_cases):
	input_number = input()

	count = [0] * 10

	for j in range(len(input_number)):
		try:
			count[int(input_number[j])] += 1
		except Exception as e:
			continue

	for j in range(1, 10):
		if count[j] != 0:
			print(j, end="")
			count[j] -= 1
			break

	for j in range(count[0]):
		print(0, end="")

	for j in range(1, 10):
		for k in range(count[j]):
			print(j, end="")

	print("")
	

###Works if the string does not have "/r"
# n_cases = int(input())

# for i in range(n_cases):
# 	input_number = input()
# 	input_number = sorted(input_number)

# 	first_non_zero_pos = -1

# 	for j in range(len(input_number)):
# 		if input_number[j] != "0":
# 			first_non_zero_pos = j
# 			break

# 	if first_non_zero_pos == 0 or first_non_zero_pos == -1:
# 		listToStr = ''.join([elem for elem in input_number])
# 	else:
# 		input_number[0] = input_number[first_non_zero_pos]
# 		input_number[first_non_zero_pos] = "0"
# 		listToStr = ''.join([elem for elem in input_number])

# 	print(int(listToStr))
