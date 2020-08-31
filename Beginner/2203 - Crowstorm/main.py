import math

while True:
	try:
		xf, yf, xi, yi, vi, r1, r2 = map(int, input().split(' '))

		tx = (xi - xf)**2
		ty = (yi - yf)**2

		d = math.sqrt(tx + ty) + (vi * 1.5)
		r = r1 + r2

		if d <= r:
			print("Y")
		else:
			print("N")
	except EOFError:
		break