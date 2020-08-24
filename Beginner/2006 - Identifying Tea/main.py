t = int(input())
a, b, c, d, e = [int(x) for x in input().split()]

count = 0

if t == a:
	count += 1
if t == b:
	count += 1
if t == c:
	count += 1
if t == d:
	count += 1
if t == e:
	count += 1
print(count)