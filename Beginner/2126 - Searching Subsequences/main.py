case = 0

while True:
	try:
		sub_s = str(input())
		full_s = str(input())

		case += 1

		j = 0
		max_j = len(sub_s)
		count = 0
		pos_sub = -1
		for i in range(len(full_s)):
			if j == max_j:
				count += 1
				j = 0
				pos_sub = i - max_j + 1

				if full_s[i - 1] == sub_s[j]:
					j += 1

			if j >= max_j:
				j = 0

			if full_s[i] == sub_s[j]:
				j += 1
			else:
				j = 0
				if full_s[i] == sub_s[j]:
					j += 1

		if j == max_j:
			count += 1
			j = 0
			pos_sub = len(full_s) - max_j + 1

		print("Caso #%d:" % case)
		if count > 0:
			print("Qtd.Subsequencias: %d" % count)
			print("Pos: %d" % pos_sub)
		else:
			print("Nao existe subsequencia")
		print("")
	except EOFError:
		break