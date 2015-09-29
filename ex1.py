i = 0
while i+1 < len(A):
	A[i], A[i+1] = A[i+1], A[i]
	i += 2
