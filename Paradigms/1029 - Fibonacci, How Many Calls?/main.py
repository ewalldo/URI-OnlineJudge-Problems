value = int(input())

values = [0] * 41
call_s = [1] * 40

values[1] = 1

for i in range(2, 41):
	values[i] = values[i - 1] + values[i - 2]
for i in range(2, 40):
	call_s[i] = values[i + 1] * 2 - 1

for i in range(value):
	fibo = int(input())
	
	print("fib(" + str(fibo) + ") = " + str(call_s[fibo] - 1) + " calls = " + str(values[fibo]))
