n_runes, min_friendship = map(int, input().split(' '))
rune_dict = {}

for i in range(n_runes):
	rune_name, rune_value = input().split(' ')
	rune_dict[rune_name] = int(rune_value)

runes_recited_total = int(input())
runes_recited = input().split(' ')

friendship = 0
for i in range(runes_recited_total):
	friendship += rune_dict[runes_recited[i]]

print(friendship)
if friendship >= min_friendship:
	print("You shall pass!")
else:
	print("My precioooous")
