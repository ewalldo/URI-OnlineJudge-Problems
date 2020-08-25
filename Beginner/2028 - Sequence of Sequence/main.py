all_values = []
all_values.append(0)

for i in range(0, 201):
	for j in range(i):
		all_values.append(i)

case_count = 0
while True:
	try:
		value = int(input())
		case_count += 1
		count = 1
		if value == 0:
			print("Caso %d: 1 numero" % case_count)
			print(all_values[0])
			print("")
		else:
			for i in range(1, value + 1):
				count += i
			print("Caso %d: %d numeros" % (case_count, count))
			for i in range(count - 1):
				print(str(all_values[i]) + " ", end="")
			print(all_values[count - 1])
			print("")
	except EOFError:
		break