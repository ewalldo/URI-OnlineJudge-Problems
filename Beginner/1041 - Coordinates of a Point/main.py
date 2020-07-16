x, y = [float(x) for x in input().split()]

if ((x == 0) or (y == 0)):
	if (x != 0):
		print("Eixo X")
	elif (y != 0):
		print("Eixo Y")
	else:
		print("Origem")
elif ((x > 0) and (y > 0)):
	print("Q1")
elif ((x > 0) and (y < 0)):
	print("Q4")
elif ((x < 0) and (y > 0)):
	print("Q2")
else:
	print("Q3")
