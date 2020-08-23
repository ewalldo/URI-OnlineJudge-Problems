aux = input()
value = int(aux)

for i in range(value):
	aux = input()
	year = int(aux)

	if year <= 2014:
		print("%d D.C." % (2015 - year))
	else:
		print("%d A.C." % (year - 2015 + 1))