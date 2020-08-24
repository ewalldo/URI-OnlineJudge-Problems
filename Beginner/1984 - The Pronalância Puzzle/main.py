aux = input()
name = int(aux)

value = str(name)
size = len(value)

for i in range(size):
	print(value[size - i - 1], end='')
print("")