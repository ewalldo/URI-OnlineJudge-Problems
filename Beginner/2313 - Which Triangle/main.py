A, B, C = [int(x) for x in input().split()]

side = [A, B, C]
side = sorted(side)

A = side[2]
B = side[1]
C = side[0]
if A >= B + C:
	print("Invalido")
else:
	if A == B and B == C and A == C:
		print("Valido-Equilatero")
	elif (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
		print("Valido-Isoceles")
	else:
		print("Valido-Escaleno")

	if (A*A) == (B*B) + (C*C):
		print("Retangulo: S")
	else:
		print("Retangulo: N")