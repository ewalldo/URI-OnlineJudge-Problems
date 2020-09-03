while True:
	values = input().split(' ')

	m = int(values[0])
	n = int(values[1])

	if m == n == 0:
		break

	out_str = str(m + n).replace('0','')
	print(out_str)