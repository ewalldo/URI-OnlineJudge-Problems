current_lower = input()

while True:
	try:
		name = input()

		if name.lower() > current_lower.lower():
			current_lower = name
	except EOFError:
		print(current_lower)
		break