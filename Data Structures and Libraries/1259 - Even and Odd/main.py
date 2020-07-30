n_numbers = int(input())

even_list = []
size_even = 0
odd_list = []
size_odd = 0

for i in range(n_numbers):
	n = int(input())

	if (n % 2 == 0):
		even_list.append(n)
		size_even += 1
	else:
		odd_list.append(n)
		size_odd += 1

even_list = sorted(even_list)
odd_list = sorted(odd_list)

for i in range(size_even):
	print(even_list[i])

for i in range(size_odd):
	print(odd_list[-(i + 1)])
