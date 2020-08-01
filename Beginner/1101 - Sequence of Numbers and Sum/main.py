while True:
	aux = input()
	name = str(aux)
	line = name.strip().split(' ')
	x1 = int(line[0])
	x2 = int(line[1])

	if x1 <= 0 or x2 <= 0:
		break

	if x1 == x2:
		print("%d Sum=%d" % (x1, x2))
		continue

	if x1 > x2:
		temp = x2
		x2 = x1
		x1 = temp

	soma = 0
	for i in range(x1, x2 + 1):
		soma += i
		print("%d " % (i), end='')
	print("Sum=" + str(soma))
