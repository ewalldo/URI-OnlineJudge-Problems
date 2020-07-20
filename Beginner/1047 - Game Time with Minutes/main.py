a, c, b, d = [int(x) for x in input().split()]

if (a > b):
	a = 24 - a;
	a += b;
elif (a == b):
	if c >= d:
		a = 24;
	else:
		a = 0
else:
	a = b - a;

if (c > d):
	c = 60 - c;
	c += d;
	a -= 1;
elif (c == d):
	c = 0;
else:
	c = d - c;

print("O JOGO DUROU " + str(a) + " HORA(S) E " + str(c) + " MINUTO(S)")
