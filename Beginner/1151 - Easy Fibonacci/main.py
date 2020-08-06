aux = input()
value = int(aux)

prev = 0
act = 1
for i in range(value):
	if i == 0 and value == 1:
		print(str(0))
	elif i == 0:
		print(str(0) + " ", end='')
	elif i == 1 and value == 2:
		print(str(1))
	elif i == 1:
		print(str(1) + " ", end='')
	else:
		fib = act + prev
		if i != value - 1:
			print("%d " % (fib), end='')
		else:
			print("%d" % (fib))
		prev = act
		act = fib
