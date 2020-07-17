n_cases = int(input())

for i in range(n_cases):
	attack = input().split('me')

	first_a_count = len(attack[0][1:])
	sec_a_count = len(attack[1][1:])

	out_str = "k" + ("a" * (first_a_count * sec_a_count))

	print(out_str)
