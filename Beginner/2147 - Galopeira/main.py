aux = input()
size = int(aux)

for i in range(size):
	aux = input()
	name = str(aux)
	leng = len(name)
	leng /= 100
	print("%.2f" % leng)