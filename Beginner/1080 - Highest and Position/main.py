maior = -1
pos = -1
for i in range(100):
	aux = input()
	value = int(aux)
	if value > maior:
		maior = value
		pos = i
print(maior)
print(pos + 1)
