s, t, f = [int(x) for x in input().split()]

total = s + t + f
if total <= 23 and total >= 0:
	print(total)
elif total >= 24:
	print(total - 24)
else:
	print(total + 24)