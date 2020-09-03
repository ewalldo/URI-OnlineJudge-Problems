while True:
	try:
		value = int(input())

		if (value >= 0 and value < 90) or value == 360:
			print("Bom Dia!!")
		elif value >= 90 and value < 180:
			print("Boa Tarde!!")
		elif value >= 180 and value < 270:
			print("Boa Noite!!")
		elif value >= 270 and value < 360:
			print("De Madrugada!!")
	except EOFError:
		break