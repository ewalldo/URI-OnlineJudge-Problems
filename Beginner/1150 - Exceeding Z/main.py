aux = input()
x = int(aux)

while True:
	aux = input()
	z = int(aux)

	if z > x:
		break

count = 2
value = x + 1
while True:
	if x + value < z:
		count += 1
		x = x + value
		value += 1
	else:
		break
print(count)
