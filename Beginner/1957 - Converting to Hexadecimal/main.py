aux = input()
value = int(aux)

hex_l = []
while value > 0:
	r = value % 16
	value = int(value / 16)
	if r < 10:
		hex_l.append(str(r))
	elif r == 10:
		hex_l.append("A")
	elif r == 11:
		hex_l.append("B")
	elif r == 12:
		hex_l.append("C")
	elif r == 13:
		hex_l.append("D")
	elif r == 14:
		hex_l.append("E")
	elif r == 15:
		hex_l.append("F")
hex_l = reversed(hex_l)
print(''.join(hex_l))