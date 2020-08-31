aux = input()
value = str(aux)

par = True
for i in range(len(value)):
	if value[i] == '1':
		if par == True:
			par = False
		else:
			par = True
if par == True:
	print(value + str(0))
else:
	print(value + str(1))