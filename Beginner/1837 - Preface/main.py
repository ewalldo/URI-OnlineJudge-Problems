aux = input()
line = str(aux)
line = line.strip().split()

a = int(line[0])
b = int(line[1])
r = a % abs(b)

for q in range(-1000, 1001):
	if b * q + r == a:
		print("%d %d" % (q, r))
		break