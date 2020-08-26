t, a = [int(x) for x in input().split()]

for i in range(a):
	aux = input()
	name = str(aux)
	if name == "fechou":
		t += 1
	elif name == "clicou":
		t -= 1
print(t)