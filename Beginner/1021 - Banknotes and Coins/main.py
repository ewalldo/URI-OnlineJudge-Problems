x = float(input())
x *= 100
x = int(round(x))

print("NOTAS:")

notas = x // 10000
print("%d nota(s) de R$ 100.00" % (notas))
x -= (notas * 10000)

notas = x // 5000
print("%d nota(s) de R$ 50.00" % (notas))
x -= (notas * 5000)

notas = x // 2000
print("%d nota(s) de R$ 20.00" % (notas))
x -= (notas * 2000)

notas = x // 1000
print("%d nota(s) de R$ 10.00" % (notas))
x -= (notas * 1000)

notas = x // 500
print("%d nota(s) de R$ 5.00" % (notas))
x -= (notas * 500)

notas = x // 200
print("%d nota(s) de R$ 2.00" % (notas))
x -= (notas * 200)

print("MOEDAS:")

notas = x // 100
print("%d moeda(s) de R$ 1.00" % (notas))
x -= (notas * 100)

notas = x // 50
print("%d moeda(s) de R$ 0.50" % (notas))
x -= (notas * 50)

notas = x // 25
print("%d moeda(s) de R$ 0.25" % (notas))
x -= (notas * 25)

notas = x // 10
print("%d moeda(s) de R$ 0.10" % (notas))
x -= (notas * 10)

notas = x // 5
print("%d moeda(s) de R$ 0.05" % (notas))
x -= (notas * 5)

print("%d moeda(s) de R$ 0.01" % (x))
