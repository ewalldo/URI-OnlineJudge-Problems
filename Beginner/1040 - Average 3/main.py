x, y, z, w = [float(x) for x in input().split()]

x *= 2
y *= 3
z *= 4

media = (x + y + z + w) / 10.0

print("Media: %.1f" % (media))

if media >= 7.0:
	print("Aluno aprovado.")
elif media < 5.0:
	print("Aluno reprovado.")
else:
	print("Aluno em exame.")
	exame = float(input())

	print("Nota do exame: %.1f" % (exame))
	media = (media + exame) / 2.0

	if media >= 5.0:
		print("Aluno aprovado.")
	else:
		print("Aluno reprovado.")
	print("Media final: %.1f" % (media))
