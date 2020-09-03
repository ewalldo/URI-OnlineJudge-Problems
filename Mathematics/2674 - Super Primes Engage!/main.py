import math

def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

while True:
	try:
		number = int(input())

		if is_prime(number):
			is_super = True
			for digit in str(number):
				if digit not in "2357":
					print("Primo")
					is_super = False
					break
			if is_super:
				print("Super")
		else:
			print("Nada")
	except EOFError:
		break