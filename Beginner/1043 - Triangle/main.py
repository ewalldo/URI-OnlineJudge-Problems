aux = input()
name = str(aux)

line = name.strip().split(' ')
A = float(line[0])
B = float(line[1])
C = float(line[2])

if (((abs(B - C) < A) & (A < B + C)) & ((abs(A - C) < B) & (B < A + C)) & ((abs(A - B) < C) & (C < A + B))):
	per = A + B + C
	print("Perimetro = %.1f" % (per))
else:
	area = ((A + B) * C) / 2
	print("Area = %.1f" % (area))
