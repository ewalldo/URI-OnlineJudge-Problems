from decimal import Decimal

value = float(input())

sign = ""
if value >= 0:
	sign = "+"

value = float(value)

mant = '{0:.4E}'.format(Decimal(value))
half = mant.split('E')
mant = half[0] + "E"
expoe = half[1]
sec_sign = expoe[0]
expoe = abs(int(expoe))
if mant == "0.0000E" or mant == "-0.0000E":
	expoe = 0
	if mant == "-0.0000E":
		sign = ""
print("%s%s%s%.2d" % (sign, mant, sec_sign, expoe))