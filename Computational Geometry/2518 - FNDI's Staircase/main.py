import math

while True:
	try:
		n_steps = int(input())

		h, c, l = map(int, input().split(' '))

		h /= 100
		c /= 100
		l /= 100

		hc = math.sqrt((c**2) + (h**2))

		print("%.4f" % (l * ((n_steps) * hc)))
	except EOFError:
		break
