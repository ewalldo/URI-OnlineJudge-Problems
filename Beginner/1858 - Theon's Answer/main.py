aux = input()
n = int(aux)

aux = input()
p = str(aux)
line = p.strip().split()
menor = 21
pessoa = -1
for i in range(n):
	value = int(line[i])
	if value < menor:
		menor = value
		pessoa = i + 1
print(pessoa)