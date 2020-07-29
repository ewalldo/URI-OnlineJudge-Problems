aux = input()
name = int(aux)
for i in range(name):
	aux = input()
	values = str(aux)
	values = values.strip().split(' ')
	a = float(values[0]) * 2
	b = float(values[1]) * 3
	c = float(values[2]) * 5
	total = (a + b + c) / (2 + 3 + 5)
	print("%.1f" % (total))
