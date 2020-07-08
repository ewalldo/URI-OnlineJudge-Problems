while True:
	try:
		phrase = input()
		out_phrase = ""
		
		for i in range(len(phrase)):
			if phrase[i] == '@':
				out_phrase += 'a'
			elif phrase[i] == '&':
				out_phrase += 'e'
			elif phrase[i] == '!':
				out_phrase += 'i'
			elif phrase[i] == '*':
				out_phrase += 'o'
			elif phrase[i] == '#':
				out_phrase += 'u'
			else:
				out_phrase += phrase[i]

		print(out_phrase)
	except EOFError:
		break
