v1 = int(input())
v2 = int(input())

if v1 > v2:
	temp = v1
	v1 = v2
	v2 = temp

count = 0
for i in range(v1 + 1, v2):
	if i % 2 == 1:
		count += i
print(count)
