n_input = int(input())

candidates = list(map(int, input().split(' ')))
count = 0

for i in range(n_input):
	if candidates[i] == 1:
		count += 1

print(count)
