aux = input()
size = int(aux)

aux = input()
name = str(aux)
values = name.strip().split()

m2 = 0
m3 = 0
m4 = 0
m5 = 0
for i in range(size):
	value = int(values[i])
	if value % 2 == 0:
		m2 += 1
	if value % 3 == 0:
		m3 += 1
	if value % 4 == 0:
		m4 += 1
	if value % 5 == 0:
		m5 += 1

print("%d Multiplo(s) de 2" % (m2))
print("%d Multiplo(s) de 3" % (m3))
print("%d Multiplo(s) de 4" % (m4))
print("%d Multiplo(s) de 5" % (m5))