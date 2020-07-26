aux = input()
name = int(aux)
count = 0
while True:
	if name % 2 != 0:
		print(name)
		count += 1
		if count == 6:
			break
	name +=1
