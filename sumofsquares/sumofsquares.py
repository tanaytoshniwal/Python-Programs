def sumofsquares(n):
	for i in range(1, sqrt(n)):
		for j in range(i, sqrt(n)):
			if(i*i+j*j == n):
				return(True)
			else:
				return(False)