aux = input()
n = int(aux)

for i in range(n):
	aux = input()
	line = str(aux)
	line = line.strip().split(' ')
	person = line[0]
	if person == "Thor":
		print("Y")
	else:
		print("N")