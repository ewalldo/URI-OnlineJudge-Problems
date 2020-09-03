dict_jewel = {}
while True:
	try:
		value = str(input())
		if value not in dict_jewel:
			dict_jewel[value] = 0
		else:
			dict_jewel[value] += 1
	except EOFError:
		print(len(dict_jewel))
		break