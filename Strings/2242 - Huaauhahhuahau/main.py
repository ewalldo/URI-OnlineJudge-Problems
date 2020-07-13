laugh_string = input()
vowel_list = []

for i in range(len(laugh_string)):
	if laugh_string[i] == 'a' or laugh_string[i] == 'e' or laugh_string[i] == 'i' or laugh_string[i] == 'o' or laugh_string[i] == 'u':
		vowel_list.append(laugh_string[i])

if vowel_list == vowel_list[::-1]:
	print("S")
else:
	print("N")
