n_cases = int(input())

for x in range(n_cases):
	joao_score = 0

	for j in range(3):
		score, distance = map(int, input().split(' '))
		joao_score += (score * distance)

	maria_score = 0

	for j in range(3):
		score, distance = map(int, input().split(' '))
		maria_score += (score * distance)

	if maria_score > joao_score:
		print("MARIA")
	elif joao_score > maria_score:
		print("JOAO")
	else:
		print("EMPATE")
