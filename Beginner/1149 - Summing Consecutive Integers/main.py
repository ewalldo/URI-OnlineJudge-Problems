aux = input()
value = str(aux)
line = value.strip().split(' ')
x = int(line[0])
soma = 0

for i in range(1, len(line)):
	if int(line[i]) <= 0:
		continue

	for j in range(int(line[i])):
		soma += (x + j)

print(soma)
