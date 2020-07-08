n_input = int(input())

hobbit = 0
human = 0
elf = 0
dwarf = 0
magician = 0

for i in range(n_input):
	name, race = input().split(' ')

	if race == "X":
		hobbit += 1
	elif race == "H":
		human += 1
	elif race == "E":
		elf += 1
	elif race == "A":
		dwarf += 1
	elif race == "M":
		magician += 1

print("%d Hobbit(s)" % hobbit)
print("%d Humano(s)" % human)
print("%d Elfo(s)" % elf)
print("%d Anao(s)" % dwarf)
print("%d Mago(s)" % magician)
