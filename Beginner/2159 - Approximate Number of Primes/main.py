import math

aux = input()
value = int(aux)

x1 = value / math.log(value)
x2 = x1 * 1.25506

print("%.1f %.1f" % (x1, x2))