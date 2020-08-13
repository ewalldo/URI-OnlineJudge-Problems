par = []
impar = []
npar = 0
nimpar = 0

for i in range(15):
	aux = input()
	value = int(aux)

	if value % 2 == 0:
		par.append(value)
		npar += 1
	else:
		impar.append(value)
		nimpar += 1

	if npar == 5:
		for j in range(5):
			print("par[%d] = %d" % (j, par[j]))
		npar = 0
		par = []
	elif nimpar == 5:
		for j in range(5):
			print("impar[%d] = %d" % (j, impar[j]))
		nimpar = 0
		impar = []
		
for i in range(nimpar):
			print("impar[%d] = %d" % (i, impar[i]))
for i in range(npar):
	print("par[%d] = %d" % (i, par[i]))