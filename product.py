
A=[1,2,3,4]

left = [1]*len(A)

right = [1]*len(A)

for i in range(len(A)-1):
	left[i+1] = left[i+1]*left[i]*A[i]
for i in range(len(A)-1, 0,-1): 
	right[i-1] = right[i-1]*right[i]*A[i]
for i in range(len(A)):
	print(left[i]*right[i])


