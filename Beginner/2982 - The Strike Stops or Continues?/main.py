n_cases = int(input())
grant = 0
expense = 0

for i in range(n_cases):
	who, value = input().split(' ')

	if who == "G":
		expense += int(value)
	else:
		grant += int(value)

if grant >= expense:
	print("A greve vai parar.")
else:
	print("NAO VAI TER CORTE, VAI TER LUTA!")
