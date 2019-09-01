def merge(L,R):
	P = []
	while len(L) and len(R):
		while len(R):
			if L[0]<R[0]:
				P.append(L[0])
				L.pop(0)
				break
			else:
				P.append(R[0])
				R.pop(0)
	for l in L:
		P.append(l)
	for r in R:
		P.append(r)
	return P

def MS(arr):
	if len(arr)==1:
		return arr
	L = arr[:len(arr)/2]
	R = arr[len(arr)/2:]
	#Left sorted, right sorted
	L_S = MS(L)
	R_S = MS(R)
	#Parent sorted by merging sorted children with merge() func
	P_S = merge(L_S,R_S)
	#clear memory
	L = R = L_S = R_S = [None]
	return P_S