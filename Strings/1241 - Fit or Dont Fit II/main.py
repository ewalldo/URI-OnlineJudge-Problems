n_cases = int(input())

for _ in range(n_cases):
	a, b = input().split(' ')
	len_a = len(a)
	len_b = len(b)

	if len_b > len_a:
		print("nao encaixa")
	elif b != a[-len_b:]:
		print("nao encaixa")
	else:
		print("encaixa")