num_input = int(input())

lowest = float('inf')

for i in range(num_input):
	price, weight = map(float, input().split(' '))

	value_for_one_kg = (price * 1000) / weight

	if value_for_one_kg < lowest:
		lowest = value_for_one_kg

print("%.2f" % (lowest))
