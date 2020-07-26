pos = 0
for i in range(5):
	aux = input()
	name = float(aux)
	if name % 2 == 0:
		pos += 1
print("%d valores pares" % (pos))
