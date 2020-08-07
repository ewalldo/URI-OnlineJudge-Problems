soma = 0
power = 0
for i in range(1, 40, 2):
	soma += (i / (2**power))
	power += 1
print("%.2f" % (soma))
