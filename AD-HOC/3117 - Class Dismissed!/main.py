n_students, min_students = map(int, input().split(' '))

time = list(map(int, input().split(' ')))
count = 0

for i in range(n_students):
	if time[i] <= 0:
		count += 1

if count >= min_students:
	print("YES")
else:
	print("NO")
