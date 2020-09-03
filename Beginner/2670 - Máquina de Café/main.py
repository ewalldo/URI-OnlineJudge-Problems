aux = input()
x1 = int(aux)
aux = input()
x2 = int(aux)
aux = input()
x3 = int(aux)

#andar 1
gasto_1 = 0
#gasto_1 += x1
gasto_1 += (x2 * 2)
gasto_1 += (x3 * 4)

#andar 2
gasto_2 = 0
gasto_2 += (x1 * 2)
#gasto_2 += (x2)
gasto_2 += (x3 * 2)

#andar 3
gasto_3 = 0
gasto_3 += (x1 * 4)
gasto_3 += (x2 * 2)
#gasto_3 += (x3)

gasto = [gasto_1, gasto_2, gasto_3]
gasto = sorted(gasto)
print(gasto[0])