input = open('int_data.txt', 'r')
A = readlines(input)
k = 0
max = min = A[0]
for i in range(len(A)):
	if A.index(A[i]) == 1:
		k += 1
	if A[:i].index(A[i]) == 0:
		print(A[i], A.index(A[i])
	if A.index(A[i])<A.index(min):
		min = A[i]
	if A.index(A[i])>A.index(max):
		max = A[i]
