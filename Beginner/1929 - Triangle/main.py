v1, v2, v3, v4 = [int(x) for x in input().split()]

a = v1
b = v2
c = v3

if (abs(b - c) < a and a < b + c) or (abs(a - c) < b and b < a + c) or (abs(a - b) < c and c < a + b):
	print("S")
else:
	a = v1
	b = v2
	c = v4
	if (abs(b - c) < a and a < b + c) or (abs(a - c) < b and b < a + c) or (abs(a - b) < c and c < a + b):
		print("S")
	else:
		a = v1
		b = v3
		c = v4
		if (abs(b - c) < a and a < b + c) or (abs(a - c) < b and b < a + c) or (abs(a - b) < c and c < a + b):
			print("S")
		else:
			a = v2
			b = v3
			c = v4
			if (abs(b - c) < a and a < b + c) or (abs(a - c) < b and b < a + c) or (abs(a - b) < c and c < a + b):
				print("S")
			else:
				print("N")