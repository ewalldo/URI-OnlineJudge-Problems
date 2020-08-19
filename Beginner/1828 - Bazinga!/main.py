aux = input()
value = int(aux)

for i in range(value):
	aux = input()
	line = str(aux)
	line = line.strip().split()

	sheldon = line[0]
	raj = line[1]

	if (sheldon == "tesoura" and raj == "papel") or (sheldon == "papel" and raj == "pedra") or (sheldon == "pedra" and raj == "lagarto") or (sheldon == "lagarto" and raj == "Spock") or (sheldon == "Spock" and raj == "tesoura") or (sheldon == "tesoura" and raj == "lagarto") or (sheldon == "lagarto" and raj == "papel") or (sheldon == "papel" and raj == "Spock") or (sheldon == "Spock" and raj == "pedra") or (sheldon == "pedra" and raj == "tesoura"):
		print("Caso #%d: Bazinga!" % (i + 1))
	elif (raj == "tesoura" and sheldon == "papel") or (raj == "papel" and sheldon == "pedra") or (raj == "pedra" and sheldon == "lagarto") or (raj == "lagarto" and sheldon == "Spock") or (raj == "Spock" and sheldon == "tesoura") or (raj == "tesoura" and sheldon == "lagarto") or (raj == "lagarto" and sheldon == "papel") or (raj == "papel" and sheldon == "Spock") or (raj == "Spock" and sheldon == "pedra") or (raj == "pedra" and sheldon == "tesoura"):
		print("Caso #%d: Raj trapaceou!" % (i + 1))
	else:
		print("Caso #%d: De novo!" % (i + 1))