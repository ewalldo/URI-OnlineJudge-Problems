n_words = int(input())

words = input().split(' ')
out_str = ""

for word in words:
	if word[:2] in ["OB", "UR"] and len(word) == 3:
		out_str += (word[:2] + "I ")
	else:
		out_str += (word + " ")

print(out_str[:-1])