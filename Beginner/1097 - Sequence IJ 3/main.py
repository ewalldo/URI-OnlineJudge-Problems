i = 1
j = 7

while True:
	print("I=%d J=%d" % (i, j))
	j -= 1
	print("I=%d J=%d" % (i, j))
	j -= 1
	print("I=%d J=%d" % (i, j))
	if i == 9 and j == 13:
		break
	i += 2
	j += 4
