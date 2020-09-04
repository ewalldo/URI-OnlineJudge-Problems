def find_longest_substring(string_a, string_b):
	substr_len = min(map(len, (string_a, string_b)))
	if len(string_a) > len(string_b):
		string_a, string_b = string_b, string_a
	for char in range(substr_len, 0, -1):
		for idx in range(0, len(string_a) - char + 1):
			if string_a[idx:idx+char] in string_b:
				return char
	return 0

while True:
	try:
		string_a = input()
		string_b = input()

		len_longest = find_longest_substring(string_a, string_b)
		print(len_longest)
	except EOFError:
		break