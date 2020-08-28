aux = input()
value = int(aux)

x1 = pow((1 + pow(5, 1/2)) / 2, value)
x2 = pow((1 - pow(5, 1/2)) / 2, value)
fib = (x1 - x2) / pow(5, 1/2)

print("%.1f" % (fib))