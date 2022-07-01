def zeros(n):
	if n < 5:
		return 0
	return n // 5 + zeros(n // 5)
