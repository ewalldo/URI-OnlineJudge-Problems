while True:
	try:
		n_code = int(input())

		for i in range(n_code):
			code = input().split(' ')
			count_last_dots = len(code[-1])
			count_spaces = len(code) - 1

			print(chr(97 + count_last_dots + (count_spaces * 3) - 1))
	except EOFError:
		break
