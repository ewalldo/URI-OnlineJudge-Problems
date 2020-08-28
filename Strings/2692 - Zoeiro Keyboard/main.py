n_letters, n_phrases = map(int, input().split(' '))
exchange_dict = {}

for _ in range(n_letters):
	letters = input()
	exchange_dict[letters[0]] = letters[2]
	exchange_dict[letters[2]] = letters[0]

for _ in range(n_phrases):
	phrase = input()
	out_str = ""

	for i in phrase:
		if i in exchange_dict.keys():
			out_str += exchange_dict[i]
		else:
			out_str += i

	print(out_str)