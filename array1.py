A = [-2,3,4,6,1,9]
target = 13
def two_sums_brute(A,target):
	for i in range(len(A)-1):
		for j in range(i+1, len(A)):
			sum = A[i]+A[j]
			if sum == target:
				print(A[i],A[j])

two_sums_brute(A,target)