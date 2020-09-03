while True:
	try:
		n, d = [int(x) for x in input().split()]
		datas = []
		for i in range(d):
			aux = input()
			name = str(aux)
			datas.append(name)
		for i in range(d):
			flag = 0
			line = datas[i].strip().split()
			for j in range(n):
				if int(line[j + 1]) == 0:
					flag = 1
				if flag == 1:
					break
			if flag == 0:
				print(line[0])
				break
		if flag == 1:
			print("Pizza antes de FdI")
	except EOFError:
		break