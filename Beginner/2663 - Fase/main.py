total = int(input())
classif = int(input())
comp = []

for _ in range(total):
	value = int(input())
	comp.append(value)
comp = sorted(comp)
now = comp[total - 1]
count = 1
for i in range(total - 2, -1, -1):
	if count >= classif and now != comp[i]:
		break
	else:
		count += 1
		now = comp[i]
print(count)