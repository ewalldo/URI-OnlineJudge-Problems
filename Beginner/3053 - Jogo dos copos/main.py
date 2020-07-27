n_movements = int(input())
curr_pos = input()

for i in range(n_movements):
	curr_movement = input()

	if curr_movement == "1":
		if curr_pos == "A":
			curr_pos = "B"
		elif curr_pos == "B":
			curr_pos = "A"
	elif curr_movement == "2":
		if curr_pos == "B":
			curr_pos = "C"
		elif curr_pos == "C":
			curr_pos = "B"
	elif curr_movement == "3":
		if curr_pos == "A":
			curr_pos = "C"
		elif curr_pos == "C":
			curr_pos = "A"

print(curr_pos)
