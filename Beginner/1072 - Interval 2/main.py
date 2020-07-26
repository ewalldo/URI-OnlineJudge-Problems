aux = input()
name = int(aux)
i_in = 0
i_out = 0
for i in range(name):
	aux = input()
	value = int(aux)
	if value >= 10 and value <= 20:
		i_in += 1
	else:
		i_out += 1
print("%d in" % (i_in))
print("%d out" % (i_out))
