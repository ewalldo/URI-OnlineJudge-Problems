while True:
	try:
		m, d = [int(x) for x in input().split()]
		if m == 12 and d == 25:
			print("E natal!")
		elif m == 12 and d == 24:
			print("E vespera de natal!")
		elif m == 12 and d > 25:
			print("Ja passou!")
		else:
			r = 360
			if m == 2:
				r -= 31
			elif m == 3:
				r -= 31 + 29
			elif m == 4:
				r -= 31 + 29 + 31
			elif m == 5:
				r -= 31 + 29 + 31 + 30
			elif m == 6:
				r -= 31 + 29 + 31 + 30 + 31
			elif m == 7:
				r -= 31 + 29 + 31 + 30 + 31 + 30
			elif m == 8:
				r -= 31 + 29 + 31 + 30 + 31 + 30 + 31
			elif m == 9:
				r -= 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31
			elif m == 10:
				r -= 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30
			elif m == 11:
				r -= 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
			elif m == 12:
				r -= 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
			r -= d
			print("Faltam %d dias para o natal!" % (r))
	except EOFError:
		break