codigo, n = [int(x) for x in input().split()]

if (codigo == 1):
	print("Total: R$ %.2f" % (n * 4.00))
elif (codigo == 2):
	print("Total: R$ %.2f" % (n * 4.50))
elif (codigo == 3):
	print("Total: R$ %.2f" % (n * 5.00))
elif (codigo == 4):
	print("Total: R$ %.2f" % (n * 2.00))
else:
	print("Total: R$ %.2f" % (n * 1.50))
