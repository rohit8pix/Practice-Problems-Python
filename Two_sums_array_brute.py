A = [-2,3,4,6,1,9,1,98,67,30,-5,-6,-8]
target = -20
def product_brute(A,target):
	for i in range(len(A)-1):
		for j in range(i+1, len(A)):
			if A[i]+A[j] == target:
				print(A[i],A[j])
				return True
	
	return False

print(product_brute(A,target))

#time compleity O(n2) - two for loops
#space complexity is O(1) no extra data structures being used 

# TWO POINTER ALGORITHM O(n) 


'''A = [0,4,5,6]
target = 11
start = 0
end = len(A)-1
result = []*2

while start<end:
	sum = A[start]+A[end]
	if sum == target:
		result.append(A[start])
		result.append(A[end])
		break
	elif sum<target:
		start+=1
	else:
		end-=1


print(result)'''