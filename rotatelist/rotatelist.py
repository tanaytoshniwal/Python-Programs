def rotatelist(l,k):
	(i,t) = (1,l)
	while i<=k:
		(l,i) = (l[len(l)-1:len(l)] + l[0:len(l)-1],i+1)
	(rot,l) = (l,t)
	return rot