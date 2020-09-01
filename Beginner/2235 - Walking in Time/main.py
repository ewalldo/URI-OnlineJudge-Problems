v1, v2, v3 = [int(x) for x in input().split()]

if v1 == v2 or v1 == v3 or v2 == v3:
	print("S")
elif v1 == v2 + v3 or v2 == v1 + v3 or v3 == v2 + v1:
	print("S")
else:
	print("N")