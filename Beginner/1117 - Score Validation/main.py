valid_val = 0
while True:
	aux = input()
	name = float(aux)

	if name >= 0 and name <= 10:
		if valid_val == 0:
			x1 = name
			valid_val += 1
		elif valid_val == 1:
			x2 = name
			valid_val += 1
	else:
		print("nota invalida")

	if valid_val == 2:
		print("media = %.2f" % ((x1 + x2) / 2))
		break
