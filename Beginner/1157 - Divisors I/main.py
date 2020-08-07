aux = input()
name = int(aux)
for i in range(1, name + 1):
	if name % i == 0:
		print(i)
