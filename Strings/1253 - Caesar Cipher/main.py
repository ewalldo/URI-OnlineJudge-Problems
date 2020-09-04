n_cases = int(input())

for _ in range(n_cases):
	sentence = input()
	right_shift = int(input())
	out_str = ""

	if right_shift == 0:
		out_str = sentence
	else:
		for char in sentence:
			ord_value = ord(char) - right_shift
			if ord_value < ord('A'):
				ord_value += 26
			out_str += chr(ord_value)

	print(out_str)