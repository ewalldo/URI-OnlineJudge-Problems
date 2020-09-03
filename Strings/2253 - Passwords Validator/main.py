while True:
	try:
		password = input()

		if len(password) < 6 or len(password) > 32:
			lowercase, uppercase, number = -1, -1, -1
		else:
			lowercase, uppercase, number = 0, 0, 0
			for char in password:
				if char.isupper():
					uppercase += 1
				elif char.islower():
					lowercase += 1
				elif char.isdecimal():
					number += 1
				else:
					lowercase, uppercase, number = -1, -1, -1
					break

		if lowercase > 0 and uppercase > 0 and number > 0:
			print("Senha valida.")
		else:
			print("Senha invalida.")
	except EOFError:
		break