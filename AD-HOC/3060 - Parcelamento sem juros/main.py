value = int(input())
payments = int(input())

add_value = value % payments
pay_value = value // payments

if (add_value == 0):
	for i in range(payments):
		print(pay_value)
else:
	for i in range(add_value):
		print(pay_value + 1)

	for i in range(payments - add_value):
		print(pay_value)
