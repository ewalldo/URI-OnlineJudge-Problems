def rajesh_win_condition(i, j):
	if i == "tesoura":
		if j == "papel" or j == "lagarto":
			return True
	elif i == "papel":
		if j == "pedra" or j == "spock":
			return True
	elif i == "pedra":
		if j == "tesoura" or j == "lagarto":
			return True
	elif i == "lagarto":
		if j == "spock" or j == "papel":
			return True
	else:
		if j == "tesoura" or j == "pedra":
			return True

n_cases = int(input())

for _ in range(n_cases):
	inputs = input().split(' ')
	rajesh = inputs[0].lower()
	sheldon = inputs[1].lower()

	if rajesh == sheldon:
		print("empate")
	elif rajesh_win_condition(rajesh, sheldon):
		print("rajesh")
	else:
		print("sheldon")