n_cases = int(input())

for i in range(n_cases):
	input_str = input()
	count_letters = [0] * 26

	for j in range(len(input_str)):
		if input_str[j] == ' ' or input_str[j] == ',':
			continue
		else:
			count_letters[ord(input_str[j]) - 97] += 1

	zero_count = 0
	for j in range(len(count_letters)):
		if count_letters[j] != 0:
			zero_count += 1

	if zero_count == 26:
		print("frase completa")
	elif zero_count >= 13:
		print("frase quase completa")
	else:
		print("frase mal elaborada")
