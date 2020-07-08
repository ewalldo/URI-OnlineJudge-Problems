distance, diameter_1, diameter_2 = map(int, input().split(' '))

value = distance / (diameter_1 + diameter_2)

print("%.2f" % (value))
