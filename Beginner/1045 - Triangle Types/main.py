aux = input()
name = str(aux)

line = name.strip().split(' ')
A = float(line[0])
B = float(line[1])
C = float(line[2])

side = [A, B, C]
side = sorted(side)

A = side[2]
B = side[1]
C = side[0]

if A >= B + C:
	print("NAO FORMA TRIANGULO")
else:
	if (A*A) == (B*B) + (C*C):
		print("TRIANGULO RETANGULO")
	if (A*A) > (B*B) + (C*C):
		print("TRIANGULO OBTUSANGULO")
	if (A*A) < (B*B) + (C*C):
		print("TRIANGULO ACUTANGULO")
	if A == B and B == C and A == C:
		print("TRIANGULO EQUILATERO")
	if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
		print("TRIANGULO ISOSCELES")
