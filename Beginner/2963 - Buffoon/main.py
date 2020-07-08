n_cases = int(input())

carlos_score = int(input())
big_score = -1

for i in range(n_cases - 1):
	score = int(input())

	if score > big_score:
		big_score = score

if carlos_score >= big_score:
	print("S")
else:
	print("N")
