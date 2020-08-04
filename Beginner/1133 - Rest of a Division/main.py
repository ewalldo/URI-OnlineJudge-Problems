aux = input()
x1 = int(aux)

aux = input()
x2 = int(aux)

if x1 > x2:
	temp = x2
	x2 = x1
	x1 = temp

if x1 == x2:
	print(0)

soma = 0
for i in range(x1 + 1, x2 ):
	if i % 5 == 2 or i % 5 == 3:
		print(i)
