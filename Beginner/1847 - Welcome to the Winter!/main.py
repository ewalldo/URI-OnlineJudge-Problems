a, b, c = [int(x) for x in input().split()]

if a > b and b <= c:
	print(":)")
elif a < b and b >= c:
	print(":(")
elif a < b and b < c and (b - a > c - b):
	print(":(")
elif a < b and b < c and (b - a <= c - b):
	print(":)")
elif a > b and b > c and (a - b > b - c):
	print(":)")
elif a > b and b > c and (a - b <= b - c):
	print(":(")
elif a == b and b < c:
	print(":)")
elif a == b and c < b:
	print(":(")
else:
	print(":(")