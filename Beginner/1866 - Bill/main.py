aux = input()
value = int(aux)

for i in range(value):
	aux = input()
	s = int(aux)

	if s % 2 == 0:
		print(0)
	else:
		print(1)