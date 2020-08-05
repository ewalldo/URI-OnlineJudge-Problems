aux = input()
value = str(aux)
line = value.strip().split(' ')
x1 = int(line[0])
x2 = int(line[1])

count = 0
for i in range(1, x2 + 1):
	if count < x1 - 1:
		print("%d " % (i), end='')
	else:
		print("%d" % (i))
	count += 1
	if count == x1:
		count = 0
