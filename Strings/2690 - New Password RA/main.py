n_cases = int(input())

for _ in range(n_cases):
	og_password = input()

	new_password = ""

	for char in og_password:
		if char in ["G", "Q", "a", "k", "u"]:
			new_password += "0"
		elif char in ["I", "S", "b", "l", "v"]:
			new_password += "1"
		elif char in ["E", "O", "Y", "c", "m", "w"]:
			new_password += "2"
		elif char in ["F", "P", "Z", "d", "n", "x"]:
			new_password += "3"
		elif char in ["J", "T", "e", "o", "y"]:
			new_password += "4"
		elif char in ["D", "N", "X", "f", "p", "z"]:
			new_password += "5"
		elif char in ["A", "K", "U", "g", "q"]:
			new_password += "6"
		elif char in ["C", "M", "W", "h", "r"]:
			new_password += "7"
		elif char in ["B", "L", "V", "i", "s"]:
			new_password += "8"
		elif char in ["H", "R", "j", "t"]:
			new_password += "9"

	print(new_password[:12])