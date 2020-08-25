pi_v = 3.14

while True:
	try:
		v = float(input())
		d = float(input())
		temp = (d / 2) * (d / 2)
		ar = pi_v * temp
		alt = v / ar
		print("ALTURA = %.2f" % alt)
		print("AREA = %.2f" % ar)
	except EOFError:
		break