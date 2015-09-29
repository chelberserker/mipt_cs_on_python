input = open('int_data.txt', 'r')
A = input.readlines()
for i in range(len(A)):
	A[i] = int(A[i])
k = 0
mx = mn = A[0]
for i in range(len(A)):
	if A[0:i].count(A[i]) == 0:
		print(A[i], A.count(A[i]), 'r', k)
		k += 1
	x = A.count(A[i])	
	if A.count(mn) > x:
		mn = A[i]
	if x > A.count(mx):
		mx = A[i]
print(mx, mn)
print(k)
