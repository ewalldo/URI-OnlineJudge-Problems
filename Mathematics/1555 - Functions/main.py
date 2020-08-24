def Rafael_function(x, y):
	return(((3*x)**2) + (y**2))

def Beto_function(x, y):
	return((2*(x**2)) + ((5*y)**2))

def Carlos_function(x, y):
	return((-100 * x) + (y**3))

n_cases = int(input())

for _ in range(n_cases):
	x, y = map(int, input().split(' '))

	Rafael_value = Rafael_function(x, y)
	Beto_value = Beto_function(x, y)
	Carlos_value = Carlos_function(x, y)

	if Rafael_value > Beto_value and Rafael_value > Carlos_value:
		print("Rafael ganhou")
	elif Beto_value > Rafael_value and Beto_value > Carlos_value:
		print("Beto ganhou")
	elif Carlos_value > Beto_value and Carlos_value > Rafael_value:
		print("Carlos ganhou")