pos = 0
for i in range(6):
	aux = input()
	name = float(aux)
	if name > 0:
		pos += 1
print("%d valores positivos" % (pos))
