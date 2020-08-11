aux = input()
name = int(aux)
for i in range(name):
	aux = input()
	value = int(aux)

	if value == 1:
		print("1 nao eh primo")
		continue

	flag = 0
	for j in range(2, int(value / 2) + 1):
		if value % j == 0:
			print("%d nao eh primo" % (value))
			flag = 1
			break

	if flag == 0:
		print("%d eh primo" % (value))
