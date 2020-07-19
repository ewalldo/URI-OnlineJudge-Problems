n_cases = int(input())

for i in range(n_cases):
	x1, y1, x2, y2 = map(int, input().split(' '))

	envelope_1 = sorted([x1, y1])
	envelope_2 = sorted([x2, y2])

	if envelope_1[0] < envelope_2[0] and envelope_1[1] < envelope_2[1]:
		print("S")
	else:
		print("N")
