while True:
	try:
		l, c = [int(x) for x in input().split()]
		pos1 = []
		pos2 = []
		found = 0
		for i in range(l):
			aux = input()
			name = str(aux)
			line = name.strip().split()
			for j in range(c):
				value = int(line[j])
				if value == 1 or value == 2:
					if found == 0:
						pos1.append(i)
						pos1.append(j)
						found += 1
					elif found == 1:
						pos2.append(i)
						pos2.append(j)
						found += 1
#				if found == 2:
#					break
#			if found == 2:
#				break
		diff1 = abs(pos1[0] - pos2[0])
		diff2 = abs(pos1[1] - pos2[1])
		print(diff1 + diff2)
	except EOFError:
		break