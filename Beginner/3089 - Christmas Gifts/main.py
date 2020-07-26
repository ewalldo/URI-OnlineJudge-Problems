while True:
	n_grandchildren = int(input())

	if n_grandchildren == 0:
		break

	present_value = list(map(int, input().split(' ')))
	pair_value = []

	for x in range(n_grandchildren):
		pair_value.append((present_value[x] + present_value[n_grandchildren * 2 - x - 1]))

	pair_value = sorted(pair_value)

	print("%d %d" % (pair_value[n_grandchildren - 1], pair_value[0]))
