a = 0
d = 0
g = 0
while True:
	aux = input()
	x1 = int(aux)

	if x1 == 1:
		a += 1
	elif x1 == 2:
		g += 1
	elif x1 == 3:
		d += 1
	elif x1 == 4:
		break


print("MUITO OBRIGADO")
print("Alcool: %d" % (a))
print("Gasolina: %d" % (g))
print("Diesel: %d" % (d))
