aux = input()
size = int(aux)

for i in range(size):
	aux = input()
	name = str(aux)
	r, g, b = [int(x) for x in input().split()]

	if name == "min":
		rgb = [r, g, b]
		rgb = sorted(rgb)
		print("Caso #%d: %d" % (i + 1, rgb[0]))
	elif name == "max":
		rgb = [r, g, b]
		rgb = sorted(rgb)
		print("Caso #%d: %d" % (i + 1, rgb[2]))
	elif name == "mean":
		print("Caso #%d: %d" % (i + 1, int((r + g + b) / 3)))
	elif name == "eye":
		print("Caso #%d: %d" % (i + 1,int((0.30 * r)+(0.59*g)+(0.11*b))))