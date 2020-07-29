import math

curr_cash, daily_expend = map(int, input().split(' '))

if (curr_cash % daily_expend) == 0:
	days = math.ceil(curr_cash / daily_expend) + 1
else:
	days = math.ceil(curr_cash / daily_expend)

if days <= 10:
	print("A UFSC fecha dia %d de setembro." % (days + 20))
else:
	print("A UFSC fecha dia %d de outubro." % (days - 10))
