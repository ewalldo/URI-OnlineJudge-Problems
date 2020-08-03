v_i = 0
v_g = 0
v_n = 0
while True:
	aux = input()
	name = str(aux)

	line = name.strip().split(' ')
	x1 = int(line[0])
	x2 = int(line[1])

	if x1 == x2:
		v_n += 1
	elif x1 > x2:
		v_i += 1
	elif x2 > x1:
		v_g += 1
	
	while True:
		print("Novo grenal (1-sim 2-nao)")
		aux = input()
		name = int(aux)
		if name == 2 or name == 1:
			break
	if name == 2:
		break
	elif name == 1:
		continue

print("%d grenais" % (v_i + v_n + v_g))
print("Inter:%d" % (v_i))
print("Gremio:%d" % (v_g))
print("Empates:%d" % (v_n))
if v_i > v_g:
	print("Inter venceu mais")
elif v_g > v_i:
	print("Gremio venceu mais")
else:
	print("Nao houve vencedor")
