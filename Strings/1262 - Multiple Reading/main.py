while True:
	try:
		trace = input()
		procs = int(input())

		while procs > 0:
			read_ops = "R" * procs
			trace = trace.replace(read_ops, 'W')
			procs -= 1

		print(len(trace))
	except EOFError:
		break
