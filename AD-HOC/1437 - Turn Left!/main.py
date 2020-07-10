while True:
	n_commands = int(input())

	if n_commands == 0:
		break

	commands = input()
	current = "N"

	for i in range(len(commands)):
		if commands[i] == "D" and current == "N":
			current = "L"
		elif commands[i] == "D" and current == "L":
			current = "S"
		elif commands[i] == "D" and current == "S":
			current = "O"
		elif commands[i] == "D" and current == "O":
			current = "N"
		elif commands[i] == "E" and current == "N":
			current = "O"
		elif commands[i] == "E" and current == "O":
			current = "S"
		elif commands[i] == "E" and current == "S":
			current = "L"
		elif commands[i] == "E" and current == "L":
			current = "N"

	print(current)
