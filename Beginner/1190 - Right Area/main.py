aux = input()
op = str(aux)

soma = 0
n = 0
for i in range(12):
	for j in range(12):
		aux = input()
		x = float(aux)
		if j > i and i + j > 11:
			soma += x
			n += 1
if op == "S":
	print("%.1f"%(soma))
else:
	print("%.1f"%(soma / n))