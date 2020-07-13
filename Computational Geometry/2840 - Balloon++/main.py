radius, amount_gas = map(int, input().split(' '))

amount_one = (4/3) * 3.1415 * (radius**3)

print(int(amount_gas // amount_one))
