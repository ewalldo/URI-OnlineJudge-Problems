while True:
	try:
		vowels = input()
		phrase = input()

		count = 0

		for vowel in vowels:
			for letter in phrase:
				if vowel == letter:
					count += 1

		print(count)
	except EOFError:
		break