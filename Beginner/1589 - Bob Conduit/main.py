aux = input()
value = int(aux)

for i in range(value):
	aux = input()
	line = str(aux)
	line = line.strip().split()
	print("%d"%(int(line[0]) + int(line[1])))