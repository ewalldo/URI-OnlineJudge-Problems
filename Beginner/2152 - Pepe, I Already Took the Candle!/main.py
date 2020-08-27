aux = input()
size = int(aux)

for i in range(size):
	h, m, s = [int(x) for x in input().split()]

	if h < 10:
		print("0%d:" % (h),end='')
	else:
		print("%d:" % (h),end='')

	if m < 10:
		print("0%d - " % (m),end='')
	else:
		print("%d - " % (m),end='')

	if s == 1:
		print("A porta abriu!")
	else:
		print("A porta fechou!")