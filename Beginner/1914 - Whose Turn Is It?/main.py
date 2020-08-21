aux = input()
value = int(aux)

for i in range(value):
	n1, e1, n2, e2 = [str(x) for x in input().split()]
	v1, v2 = [int(x) for x in input().split()]

	result = ""
	if (v1 + v2) % 2 == 0:
		result = "PAR"
	else:
		result = "IMPAR"

	if e1 == result:
		print(n1)
	elif e2 == result:
		print(n2)