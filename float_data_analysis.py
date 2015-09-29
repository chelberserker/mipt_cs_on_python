input = open('float_data.txt', 'r')
A = input.readlines()
for i in range(len(A)):
	A[i] = float(A[i])
average = sum(A)/len(A)
sumsqr = 0
for i in range(len(A)):
	sumsqr += A[i]**2
stddev = (sumsqr/len(A) - average**2)**0.5

print(average, stddev)

