value = int(input())
values = str(input()).split()

res = 1
prev_ = ""

if len(values) == 1:
	print("1")
else:
	for i in range(len(values) - 1, 0, -1):
		now_ = ""
		if int(values[i]) > int(values[i - 1]):
			now_ = "pico"
		elif int(values[i]) < int(values[i - 1]):
			now_ = "vale"
		else:
			now_ = "break"

		#print("%d: %s %s"%(i, now_, prev_))
		if now_ == prev_:
			now_ = "break"
		else:
			prev_ = now_

		if now_ == "break":
			#print(i)
			#print(values[i])
			res = 0
			break
print(res)