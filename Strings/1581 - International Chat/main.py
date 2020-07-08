n_input = int(input())

for i in range(n_input):
	n_cases = int(input())

	language = input()

	flag = False

	for j in range(n_cases - 1):
		language_2 = input()

		if language != language_2:
			flag = True

	if flag:
		print("ingles")
	else:
		print(language)
