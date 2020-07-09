import math

n_laps, n_signs = map(int, input().split(' '))

total = n_laps * n_signs
out_values = []

for i in range(1, 10):
	out_values.append(int(math.ceil(total * (i / 10))))

for i in range(8):
	print(str(out_values[i]) + " ", end="")
print(out_values[8])
