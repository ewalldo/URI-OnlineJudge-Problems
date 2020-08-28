aux = input()
value = int(aux)

temp = 2
if value == 0:
	print("%.10f" % (1))
else:
	for i in range(1, value):
		temp = 2 + (1.0 / temp)
	res = 1 + (1 / temp)
	print("%.10f" % (res))