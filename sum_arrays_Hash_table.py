A = [2,4,6,5]
target = 10

def two_sums_hash(A,target):
	ht = dict()
	for i in range(len(A)):
		if A[i] in ht:
			print(ht[A[i]],A[i])
			return True
		else:
			ht[target/A[i]]=A[i]
	return False


print(two_sums_hash(A,target))