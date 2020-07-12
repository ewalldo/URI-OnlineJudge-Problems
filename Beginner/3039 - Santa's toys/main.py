n_cases = int(input())
car_toy = 0
dolls = 0

for i in range(n_cases):
	name, gender = input().split(' ')

	if gender == "F":
		dolls += 1
	else:
		car_toy += 1

print("%d carrinhos" % car_toy)
print("%d bonecas" % dolls)
