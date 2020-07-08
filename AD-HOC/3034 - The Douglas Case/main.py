import math

def is_prime(prime_):
	for i in range(2, int(math.sqrt(prime_) + 1)):
		if prime_ % i == 0:
			return False
	return True

n_cases = int(input())

possible = []

for i in range(n_cases):
	last_case = int(input())

	current_case = last_case + 1

	if current_case % 7 != 0:
		print("No")
	elif current_case % 2 == 0:
		print("No")
	else:
		if is_prime(current_case + 2):
			print("Yes")
		else:
			print("No")
