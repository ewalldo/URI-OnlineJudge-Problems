aux = input()
name = str(aux)

line = name.strip().split(' ')
a = float(line[0])
b = float(line[1])
c = float(line[2])

if a == 0.0:
	print("Impossivel calcular")
else:
	root = (b * b) - (4 * a * c)

	if root < 0.0:
		print("Impossivel calcular")
	else:
		r1 = ((-b) + (root**(1/2))) / (2 * a)
		r2 = ((-b) - (root**(1/2))) / (2 * a)

		print("R1 = %.5f" % (r1))
		print("R2 = %.5f" % (r2))
