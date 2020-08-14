aux = input()
line = int(aux)

aux = input()
op = str(aux)

soma = 0
for i in range(12):
	for j in range(12):
		aux = input()
		x = float(aux)
		if j == line:
			soma += x
if op == "S":
	print("%.1f"%(soma))
else:
	print("%.1f"%(soma / 12))