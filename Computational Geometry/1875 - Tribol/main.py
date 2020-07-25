n_cases = int(input())

for i in range(n_cases):
	n_goal = int(input())

	goals_red = 0
	goals_green = 0
	goals_blue = 0

	for j in range(n_goal):
		scored, conceded = input().split(' ')

		if scored == "R":
			if conceded == "G":
				goals_red += 2
			else:
				goals_red += 1
		elif scored == "G":
			if conceded == "B":
				goals_green += 2
			else:
				goals_green += 1
		else:
			if conceded == "R":
				goals_blue += 2
			else:
				goals_blue += 1

	if goals_red > goals_blue and goals_red > goals_green:
		print("red")
	elif goals_green > goals_blue and goals_green > goals_red:
		print("green")
	elif goals_blue > goals_green and goals_blue > goals_red:
		print("blue")
	elif goals_red == goals_green == goals_blue:
		print("trempate")
	else:
		print("empate")
