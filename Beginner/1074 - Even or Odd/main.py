aux = input()
name = int(aux)
for i in range(name):
	aux = input()
	value = int(aux)
	if value == 0:
		print("NULL")
	elif value % 2 == 0 and value > 0:
		print("EVEN POSITIVE")
	elif value % 2 == 0 and value < 0:
		print("EVEN NEGATIVE")
	elif value > 0:
		print("ODD POSITIVE")
	else:
		print("ODD NEGATIVE")
