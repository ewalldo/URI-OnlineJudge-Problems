aux = input()
value = int(aux)

while value >= 1000:
	print("M",end='')
	value -= 1000

while value >= 500:
	if value >= 900:
		print("CM",end='')
		value -= 900
	else:
		print("D",end='')
		value -= 500

while value >= 100:
	if value >= 400:
		print("CD",end='')
		value -= 400
	else:
		print("C",end='')
		value -= 100

while value >= 50:
	if value >= 90:
		print("XC",end='')
		value -= 90
	else:
		print("L",end='')
		value -= 50

while value >= 10:
	if value >= 40:
		print("XL",end='')
		value -= 40
	else:
		print("X",end='')
		value -= 10

while value >= 5:
	if value >= 9:
		print("IX",end='')
		value -= 9
	else:
		print("V",end='')
		value -= 5

while value >= 1:
	if value >= 4:
		print("IV",end='')
		value -= 4
	else:
		print("I",end='')
		value -= 1

print("")