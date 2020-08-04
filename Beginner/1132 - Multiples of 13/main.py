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
for i in range(x1, x2 + 1):
	if i % 13 != 0:
		soma += i

print(soma)
