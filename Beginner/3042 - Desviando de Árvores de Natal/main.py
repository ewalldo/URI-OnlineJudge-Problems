while True:
	n_input = int(input())

	if n_input == 0:
		break

	curr_pos = 1
	n_touch = 0

	for i in range(n_input):
		curr_state = list(map(int, input().split(' ')))

		if curr_state[curr_pos] == 0:
			continue
		else:
			if curr_state[0] == 0:
				n_touch += abs(curr_pos - 0)
				curr_pos = 0
			elif curr_state[1] == 0:
				n_touch += abs(curr_pos - 1)
				curr_pos = 1
			elif curr_state[2] == 0:
				n_touch += abs(curr_pos - 2)
				curr_pos = 2

	print(n_touch)
