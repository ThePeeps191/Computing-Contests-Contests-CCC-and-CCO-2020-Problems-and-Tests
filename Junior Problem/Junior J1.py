def BarleyChecker(S=0, M=0, L=0):
	if S + 2 * M + 3 * L >= 10:
		return "happy"
	else:
		return "sad"
