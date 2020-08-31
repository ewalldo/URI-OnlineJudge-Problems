while True:
	v1, v2 = [int(x) for x in input().split()]

	if v1 == 0 and v2 == 0:
		break

	print(v1 * v2)