i = 0
j = 1

while True:
	for x in range(3):
		if i == 0.0 or i == 1.0 or i > 1.8:
			#if j == 1.0 or j == 2.0 or j == 3.0 or j == 4.0 or j > 4.8:
			print("I=%.0f J=%.0f" % (i, j))
			#else:
				#print("I=%.0f J=%.1f" % (i, j))
		else:
			print("I=%.1f J=%.1f" % (i, j))
		j += 1
	i += 0.2
	j -= 3
	j += 0.2
	if i > 2.0:# and j == 13:
		break
