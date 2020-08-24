while True:
	try:
		aux = input()
		time = str(aux)
		line = time.strip().split(':')
		hour = int(line[0])
		minute = int(line[1])
		hour += 1
		if (hour <= 7):
			print("Atraso maximo: 0")
		else:
			diff = (hour - 8) * 60 + minute
			print("Atraso maximo: " + str(diff))
	except EOFError:
		break