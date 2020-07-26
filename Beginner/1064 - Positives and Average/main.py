pos = 0
media = 0
for i in range(6):
	aux = input()
	name = float(aux)
	if name > 0:
		pos += 1
		media += name
media /= pos
print("%d valores positivos" % (pos))
print("%.1f" % (media))
