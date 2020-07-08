n_cases = int(input())

for i in range(n_cases):
	input_str = list(map(int, input().split(' ')))

	n_players = input_str[0]

	age_players = input_str[1:]

	print("Case %d: %d" % (i + 1, age_players[n_players // 2]))
