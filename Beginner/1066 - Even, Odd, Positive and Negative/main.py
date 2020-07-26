pos = 0
neg = 0
par = 0
imp = 0
for i in range(5):
	aux = input()
	name = float(aux)
	if name % 2 == 0:
		par += 1
	else:
		imp += 1
	if name > 0:
		pos += 1
	elif name < 0:
		neg += 1
print("%d valor(es) par(es)" % (par))
print("%d valor(es) impar(es)" % (imp))
print("%d valor(es) positivo(s)" % (pos))
print("%d valor(es) negativo(s)" % (neg))
