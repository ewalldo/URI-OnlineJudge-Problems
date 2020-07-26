test_case = 1

while True:
	n_cases = int(input())

	if n_cases == 0:
		break

	math_expression = input()
	math_op = []
	if math_expression[0] == "-":
		math_op.append("-")
		math_expression = math_expression[1:]
	else:
		math_op.append("+")

	for i in range(len(math_expression)):
		if math_expression[i] == "+":
			math_op.append("+")
		elif math_expression[i] == "-":
			math_op.append("-")

	math_expression = math_expression.replace("+", " ")
	math_expression = math_expression.replace("-", " ")
	math_expression = math_expression.split(" ")

	result = 0

	for i in range(n_cases):
		if math_op[i] == "+":
			result += int(math_expression[i])
		elif math_op[i] == "-":
			result -= int(math_expression[i])

	print("Teste " + str(test_case))
	print(result)
	print("")
	test_case += 1
