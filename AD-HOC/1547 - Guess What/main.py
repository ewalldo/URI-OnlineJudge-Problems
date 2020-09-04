n_cases = int(input())

for _ in range(n_cases):
	n_students, secret_number = map(int, input().split(' '))
	guess_numbers = input().split(' ')
	difference = []

	for number in guess_numbers:
		difference.append(abs(int(number) - secret_number))

	print(difference.index(min(difference)) + 1)