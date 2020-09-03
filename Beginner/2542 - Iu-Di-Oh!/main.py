while True:
	try:
		n_atrb = int(input())
		n_m, n_l = [int(x) for x in input().split()]
		m_deck = []
		l_deck = []
		for _ in range(n_m):
			values = str(input()).split()
			values = list(map(int, values))
			m_deck.append(values)
		for _ in range(n_l):
			values = str(input()).split()
			values = list(map(int, values))
			l_deck.append(values)
		c_m, c_l = [int(x) for x in input().split()]
		c_atrb = int(input())

		m_v = m_deck[c_m - 1][c_atrb - 1]
		l_v = l_deck[c_l - 1][c_atrb - 1]

		if m_v > l_v:
			print("Marcos")
		elif m_v < l_v:
			print("Leonardo")
		else:
			print("Empate")
	except EOFError:
		break