n_cases = int(input())

for i in range(n_cases):
	shopping_list = input().split(' ')
	shopping_dict = {}

	for j in range(len(shopping_list)):
		shopping_dict[shopping_list[j]] = 1

	dictionary_items = shopping_dict.items()
	dictionary_items = sorted(dictionary_items)

	out_str = ""
	for j in range(len(dictionary_items)):
		if out_str != "":
			out_str += (" " + dictionary_items[j][0])
		else:
			out_str += dictionary_items[j][0]

	print(out_str)
