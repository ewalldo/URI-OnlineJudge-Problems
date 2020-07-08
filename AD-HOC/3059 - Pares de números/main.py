n_values, min_value, max_value = map(int, input().split(' '))

values = list(map(int, input().split(' ')))
count = 0

for i in range(n_values):
	for j in range(i + 1, n_values):
		sum_value = values[i] + values[j]
		if sum_value >= min_value and sum_value <= max_value:
			count += 1

print(count)
