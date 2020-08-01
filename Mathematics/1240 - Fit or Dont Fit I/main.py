n_cases = int(input())

for i in range(n_cases):
	a, b = input().split(' ')

	if len(b) > len(a):
		print("nao encaixa")
	elif b == a[-len(b):]:
		print("encaixa")
	else:
		print("nao encaixa")
