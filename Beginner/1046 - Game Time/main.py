a, b = [int(x) for x in input().split()]

if (a > b):
	a = 24 - a;
	a += b;
	print("O JOGO DUROU " + str(a) + " HORA(S)")
elif (a == b):
	print("O JOGO DUROU 24 HORA(S)")
else:
	print("O JOGO DUROU " + str(b - a) + " HORA(S)")
