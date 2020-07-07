while True:
	try:
		size = int(input())
		d = {}
		for i in range(size):
			c, v = [str(x) for x in input().split()]
			d[int(v)] = c
		d = sorted(d.items())
		for i in range(size):
			print(d[i][1],end='')
			if i != size - 1:
				print(" ",end='')
		print("")
	except EOFError:
		break
