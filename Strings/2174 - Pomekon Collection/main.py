n_pomekon = int(input())
pomekon_list = []

for _ in range(n_pomekon):
	pomekon_list.append(input())

unique_pomekon = len(set(pomekon_list))

print("Falta(m) %d pomekon(s)." % (151 - unique_pomekon))