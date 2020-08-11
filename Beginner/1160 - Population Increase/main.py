aux = input()
size = int(aux)

for i in range(size):
	aux = input()
	line = str(aux)
	line = line.strip().split()
	pa = int(line[0])
	pb = int(line[1])
	ga = float(line[2]) / 100
	gb = float(line[3]) / 100
	count = 0
	while True:
		pa = int(pa + (pa * ga))
		pb = int(pb + (pb * gb))
		count += 1
		if pa > pb:
			print(str(count) + " anos.")
			break
		if count >= 100:
			print("Mais de 1 seculo.")
			break
