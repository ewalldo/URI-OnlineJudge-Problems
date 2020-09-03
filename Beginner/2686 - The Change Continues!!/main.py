import math

while True:
	try:
		value = float(input())

		x = (86400 * value) / 360
		h = math.trunc(x / 3600)
		m = math.trunc((x % 3600) / 60)
		s = round((x % 3600) % 60, 2)

		if (value >= 0 and value < 90) or value == 360:
			print("Bom Dia!!")
		elif value >= 90 and value < 180:
			print("Boa Tarde!!")
		elif value >= 180 and value < 270:
			print("Boa Noite!!")
		elif value >= 270 and value < 360:
			print("De Madrugada!!")
		h += 6
		if h >= 24:
			h -= 24
		print("%.2d:%.2d:%.2d" % (h, m, s))
	except EOFError:
		break