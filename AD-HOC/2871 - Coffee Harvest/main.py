while True:
	try:
		n_rows, n_cols = map(int, input().split(' '))
		total_coffe = 0

		for i in range(n_rows):
			coffe_list = input().split(' ')
			coffe_value = 0
			for j in range(n_cols):
				try:
					coffe_value += int(coffe_list[j])
				except Exception as e:
					coffe_value = coffe_value
			total_coffe += coffe_value

		sacas = int(total_coffe / 60)
		litros = total_coffe % 60

		print("%d saca(s) e %d litro(s)" % (sacas, litros))
	except EOFError:
		break
