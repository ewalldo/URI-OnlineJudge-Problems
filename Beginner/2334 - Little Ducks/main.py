while True:
	aux = input()
	l = int(aux)
	if l < 0:
		break
	elif l == 0:
		print(0)
	else:
		print(l - 1)