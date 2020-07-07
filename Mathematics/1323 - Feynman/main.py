value = int(input())

while(value != 0):
	total_squares = 0
	for i in range(value + 1):
		total_squares += (i * i)
	print(total_squares)
	value = int(input())
