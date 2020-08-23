jump, pipes = [int(x) for x in input().split()]

aux = input()
size = str(aux)
line = size.strip().split()

flag = 0
for i in range(pipes - 1):
	if abs(int(line[i]) - int(line[i + 1])) > jump:
		flag = 1
		break
if flag == 1:
	print("GAME OVER")
else:
	print("YOU WIN")