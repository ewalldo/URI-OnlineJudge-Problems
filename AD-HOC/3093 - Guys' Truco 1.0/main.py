n_cases = int(input())

for _ in range(n_cases):
	input_str = input()

	cards = [0] * 4

	for i in range(len(input_str)):
		if input_str[i] == "Q":
			cards[0] = 1
			if sum(cards) == 4:
				break
		elif input_str[i] == "J":
			cards[1] = 1
			if sum(cards) == 4:
				break
		elif input_str[i] == "K":
			cards[2] = 1
			if sum(cards) == 4:
				break
		elif input_str[i] == "A":
			cards[3] = 1
			if sum(cards) == 4:
				break

	if sum(cards) == 4:
		print("Aaah muleke")
	else:
		print("Ooo raca viu")