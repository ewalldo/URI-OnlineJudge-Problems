while True:
	try:
		value = input()

		parenthesis = []
		len_parenthesis = 0

		flag = True

		for i in range(len(value)):
			if value[i] == '(':
				parenthesis.append('(')
				len_parenthesis += 1
			elif value[i] == ')':
				if len_parenthesis <= 0:
					flag = False
					break
				elif parenthesis[len_parenthesis - 1] != '(':
					flag = False
					break
				else:
					parenthesis.pop(len_parenthesis - 1)
					len_parenthesis -= 1

		if len_parenthesis == 0 and flag:
			print("correct")
		else:
			print("incorrect")
	except EOFError:
		break
