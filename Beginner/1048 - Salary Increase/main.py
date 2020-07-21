salario = float(input())

if (salario >= 0 and salario <= 400.00):
	salarioComReajuste = (salario * 115) / 100
	reajuste = salarioComReajuste - salario

	#print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 15 %" % (salarioComReajuste, reajuste))
	print("Novo salario: %.2f" % (salarioComReajuste))
	print("Reajuste ganho: %.2f" % (reajuste))
	print("Em percentual: 15 %")
elif (salario >= 400.01 and salario <= 800.00):
	salarioComReajuste = (salario * 112) / 100
	reajuste = salarioComReajuste - salario

	print("Novo salario: %.2f" % (salarioComReajuste))
	print("Reajuste ganho: %.2f" % (reajuste))
	print("Em percentual: 12 %")
elif (salario >= 800.01 and salario <= 1200.00):
	salarioComReajuste = (salario * 110) / 100
	reajuste = salarioComReajuste - salario

	print("Novo salario: %.2f" % (salarioComReajuste))
	print("Reajuste ganho: %.2f" % (reajuste))
	print("Em percentual: 10 %")
elif (salario >= 1200.01 and salario <= 2000.00):
	salarioComReajuste = (salario * 107) / 100
	reajuste = salarioComReajuste - salario

	print("Novo salario: %.2f" % (salarioComReajuste))
	print("Reajuste ganho: %.2f" % (reajuste))
	print("Em percentual: 7 %")
else:
	salarioComReajuste = (salario * 104) / 100
	reajuste = salarioComReajuste - salario

	print("Novo salario: %.2f" % (salarioComReajuste))
	print("Reajuste ganho: %.2f" % (reajuste))
	print("Em percentual: 4 %")
