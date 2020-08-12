aux = input()
name = int(aux)
x = []

for i in range(name):
	aux = input()
	value = int(aux)
	x.append(value)

bigger = max(x)

fib = [0] * (bigger + 1)
fib[0] = 0
fib[1] = 1


for i in range(2, bigger + 1):
	fib[i] = fib[i -1] + fib[i - 2]

for i in range(len(x)):
	print("Fib(%d) = %d" % (x[i], fib[x[i]]))