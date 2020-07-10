while True:
	try:
		n_numbers = int(input())

		number_list = list(map(int, input().split(' ')))

		number_list = sorted(number_list)
		sum_number = 0

		for i in range(n_numbers // 2):
			diff = number_list[-(i+1)] - number_list[i]
			sum_number += diff

		print(sum_number)
	except EOFError:
		break
