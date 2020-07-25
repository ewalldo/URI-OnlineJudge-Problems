aux = input()
name = float(aux)

if name <= 2000.00:
	print("Isento")
else:
	name -= 2000.00
	if name <= 1000.00:
		value = name * 0.08
		print("R$ %.2f" % (value))
	elif name > 1000.00 and name <= 2500.00:
		value = 1000.00 * 0.08
		name -= 1000
		value += (name * 0.18)
		print("R$ %.2f" % (value))
	else:
		value = 1000.00 * 0.08
		value += 1500.00 * 0.18
		name -= 2500.00
		value += (name * 0.28)
		print("R$ %.2f" % (value))
