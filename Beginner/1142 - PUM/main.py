aux = input()
num = int(aux)

p = 1
for i in range(num):
	for j in range(3):
		print("%d " % (p), end='')
		p += 1
	print("PUM")
	p += 1
