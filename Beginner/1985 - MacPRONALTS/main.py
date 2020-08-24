aux = input()
name = int(aux)

total = 0
for i in range(name):
	c, q = [int(x) for x in input().split()]

	if c == 1001:
		total += 1.5 * q
	elif c == 1002:
		total += 2.5 * q
	elif c == 1003:
		total += 3.5 * q
	elif c == 1004:
		total += 4.5 * q
	elif c == 1005:
		total += 5.5 * q
print("%.2f"%(total))