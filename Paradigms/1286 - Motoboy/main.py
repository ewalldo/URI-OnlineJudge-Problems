def knapsack(max_pizza, n_pizza, time_pizza, n_values):
	K = [[0 for x in range(max_pizza + 1)] for x in range(n_values + 1)]

	for i in range(n_values + 1):
		for w in range(max_pizza + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif n_pizza[i - 1] <= w:
				K[i][w] = max(time_pizza[i - 1] + K[i - 1][w - n_pizza[i - 1]], K[i - 1][w])
			else:
				K[i][w] = K[i - 1][w]

	return K[n_values][max_pizza]

while True:
	n_deliveries = int(input())

	if n_deliveries == 0:
		break

	max_pizza = int(input())
	pizza_values = []
	pizza_time = []

	for i in range(n_deliveries):
		time, n = map(int, input().split(' '))

		pizza_time.append(time)
		pizza_values.append(n)

	print(str(knapsack(max_pizza, pizza_values, pizza_time, n_deliveries)) + " min.")
