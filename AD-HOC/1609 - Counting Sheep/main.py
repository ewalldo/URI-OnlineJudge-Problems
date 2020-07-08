n_cases = int(input())

for i in range(n_cases):
	n_sheep = int(input())

	sheep_id = list(map(int, input().split(' ')))
	sheep_count = {}
	new_sheep = 0

	for j in range(n_sheep):
		if sheep_id[j] not in sheep_count:
			sheep_count[sheep_id[j]] = True
			new_sheep += 1

	print(new_sheep)
