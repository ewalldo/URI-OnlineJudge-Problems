num_input = int(input())

if num_input > 0:
	n_students = list(map(int, input().split(' ')))
else:
	n_students = input()

n_groups = 0
for i in range(num_input):
	n_groups += (n_students[i] // 3)

print(n_groups * 3)
