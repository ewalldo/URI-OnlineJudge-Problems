aux = input()
value = int(aux)

aux = input()
line = str(aux)
line = line.strip().split()

flag = ""
for i in range(value - 1):
	if int(line[i + 1]) < int(line[i]):
		print(i + 2)
		flag = "OK"
		break

if flag != "OK":
	print(0)