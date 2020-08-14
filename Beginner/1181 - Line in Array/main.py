aux = input()
line = int(aux)

aux = input()
op = str(aux)

soma = 0
flag = 0
for i in range(12):
	for j in range(12):
		aux = input()
		x = float(aux)
		if i == line:
			soma += x
			flag = 1
	if flag == 1:
		break
if op == "S":
	print("%.1f"%(soma))
else:
	print("%.1f"%(soma / 12))