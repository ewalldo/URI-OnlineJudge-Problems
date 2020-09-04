n_cases = int(input())

for _ in range(n_cases):
	n_students = int(input())
	grades = list(map(int, input().split(' ')))
	sorted_grades = sorted(grades, reverse=True)

	not_change = 0

	for i in range(n_students):
		if grades[i] == sorted_grades[i]:
			not_change += 1

	print(not_change)