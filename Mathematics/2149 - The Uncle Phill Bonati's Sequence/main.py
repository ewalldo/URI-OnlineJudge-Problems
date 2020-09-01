def phill_bonati(n):
	phill_bonati_list = [0, 1]

	a, b = 0, 1

	for i in range(n - 1):
		if i % 2 == 0:
			a, b = b, a + b
		else:
			a, b = b, a * b
		phill_bonati_list.append(a)
	return phill_bonati_list[-1]

while True:
	try:
		n = int(input())
		
		if n == 1:
			print(0)
		else:
			print(phill_bonati(n))
	except EOFError:
		break