def wellbracketed(s):
	c=0
	for i in range(0, len(s)):
		if s[i] == "(":
			c = c + 1
		elif s[i] == ")":
			c = c - 1
	if c == 0:
		return(True)
	else:
		return(False)