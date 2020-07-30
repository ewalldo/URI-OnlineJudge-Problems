aux = input()
name = int(aux)
total_c = 0
c_r = 0
c_s = 0
c_c = 0
for i in range(name):
	aux = input()
	value = str(aux)
	value = value.strip().split(' ')
	num_c = int(value[0])
	type_c = value[1]

	total_c += num_c

	if type_c == 'R':
		c_r += num_c
	elif type_c == 'S':
		c_s += num_c
	elif type_c == 'C':
		c_c += num_c
print("Total: %d cobaias" % (total_c))
print("Total de coelhos: %d" % (c_c))
print("Total de ratos: %d" % (c_r))
print("Total de sapos: %d" % (c_s))
print("Percentual de coelhos: %.2f %%" % (c_c / total_c * 100))
print("Percentual de ratos: %.2f %%" % (c_r / total_c * 100))
print("Percentual de sapos: %.2f %%" % (c_s / total_c * 100))
