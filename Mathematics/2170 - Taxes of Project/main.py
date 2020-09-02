project_number = 1

while True:
	try:
		x, y = map(float, input().split(' '))

		interest = (y - x) / x * 100

		print("Projeto " + str(project_number) + ":")
		print("Percentual dos juros da aplicacao:", format(interest, ".2f"), "%\n")

		project_number += 1
	except EOFError:
		break