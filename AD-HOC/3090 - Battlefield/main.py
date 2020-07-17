n, m, total_soldiers = map(int, input().split(' '))

skill_army_1 = 0
skill_army_2 = 0

for i in range(total_soldiers):
	x, y, skill = map(int, input().split(' '))

	if (n*y) - (m*x) < 0:
		skill_army_1 += skill
	else:
		skill_army_2 += skill

print("%d %d" % (skill_army_2, skill_army_1))
