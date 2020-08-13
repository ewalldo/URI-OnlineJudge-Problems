aux = input()
name = int(aux)

aux = input()
name = str(aux)

line = name.strip().split()
menor = int(line[0])
pos = 0

for i in range(1, len(line)):
	value = int(line[i])
	if value < menor:
		menor = value
		pos = i
print("Menor valor: " + str(menor))
print("Posicao: " + str(pos))