aux = input()
value = int(aux)

temp = 6
if value == 0:
	print("%.10f" % (3))
else:
	for i in range(1, value):
		temp = 6 + (1.0 / temp)
	res = 3 + (1 / temp)
	print("%.10f" % (res))