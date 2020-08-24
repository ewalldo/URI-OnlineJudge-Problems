aux = input()
name = int(aux)

maior = -1
student = -1
for i in range(name):
	s, g = [float(x) for x in input().split()]
	if g > maior:
		maior = g
		student = s
if maior < 8:
	print("Minimum note not reached")
else:
	print("%.0f"%student)