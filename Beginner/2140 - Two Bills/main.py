notas = [2, 5, 10, 20, 50, 100]
possible = []
for i in range(len(notas)):
	for j in range(i, len(notas)):
		possible.append(notas[i] + notas[j])

while True:
	v1, v2 = [int(x) for x in input().split()]

	if v1 == 0 and v2 == 0:
		break

	diff = v2 - v1

	if diff in possible:
		print("possible")
	else:
		print("impossible")