while True:
	try:
		v1, v2 = [int(x) for x in input().split()]
		fat = []
		fat.append(1)
		fat.append(1)

		bigger = v1
		if v2 > v1:
			bigger = v2
		fat_now = 1
		for i in range(2, bigger + 1):
			fat_now = fat_now * i
			fat.append(fat_now)
		print(fat[v1] + fat[v2])
	except EOFError:
		break
