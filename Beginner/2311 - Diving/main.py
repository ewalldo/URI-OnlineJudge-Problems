aux = input()
size = int(aux)

for i in range(size):
	aux = input()
	name = str(aux)
	aux = input()
	diff = float(aux)
	s1, s2, s3, s4, s5, s6, s7 = [float(x) for x in input().split()]
	s = [s1, s2, s3, s4, s5, s6, s7]
	s = sorted(s)
	total = 0
	for i in range(1, len(s) - 1):
		total += s[i]
	total *= diff
	print("%s %.2f" % (name, total))