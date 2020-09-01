biggest = ""
len_biggest = 0

while True:
	phrase = input().split(' ')

	if phrase[0] == "0":
		break

	word_len = ""

	for word in phrase:
		len_word = len(word)
		word_len += str(len_word) + "-"

		if len_word >= len_biggest:
			biggest = word
			len_biggest = len_word

	print(word_len[:-1])
print("\nThe biggest word: " + biggest)