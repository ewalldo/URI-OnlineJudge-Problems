aux = input()
size = int(aux)

s1t = s2t = b1t = b2t = a1t = a2t = 0
for i in range(size):
	aux = input()
	name = str(aux)
	s1, b1, a1 = [int(x) for x in input().split()]
	s2, b2, a2 = [int(x) for x in input().split()]
	s1t += s1
	s2t += s2
	b1t += b1
	b2t += b2
	a1t += a1
	a2t += a2
ps = s2t / s1t * 100
pb = b2t / b1t * 100
pa = a2t / a1t * 100
print("Pontos de Saque: %.2f %%." % (ps))
print("Pontos de Bloqueio: %.2f %%." % (pb))
print("Pontos de Ataque: %.2f %%." % (pa))