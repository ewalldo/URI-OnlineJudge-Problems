n_cases = int(input())

for i in range(n_cases):
	message = input()
	decoded = ""

	for j in range(len(message)):
		if message[j].islower():
			decoded += message[j]

	print(decoded[::-1])
