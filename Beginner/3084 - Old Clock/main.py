while True:
	try:
		hour, minute = map(int, input().split(' '))

		hour = int(hour / 30)
		minute = int(minute / 6)

		print("%02d:%02d" % (hour, minute))
	except EOFError:
		break
