while True:
	try:
		t, a, w, c = map(int, input().split())

		w /= 100.
		c /= 100.
		now = a / t

		if now >= c:
			print("critical")
		elif now >= w:
			print("warning")
		else:
			print("OK")
	except EOFError:
		break
