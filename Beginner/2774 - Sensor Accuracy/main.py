while True:
	try:
		v1, v2 = [int(x) for x in input().split()]
		values = str(input()).split()
		values = list(map(float, values))
		size_array = len(values)
		avg = sum(values) / size_array
		sum_a = 0
		for i in range(size_array):
			sum_a += ((values[i] - avg)**2)
		out = (sum_a / (size_array - 1))**0.5
		print("%.5f" % (out))
	except EOFError:
		break