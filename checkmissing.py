A= [0,1,3,4]


sum_1 = 0
sum_2 = 0
for i in range(len(A)):
	sum_1 = sum_1 + A[i]
for i in range(len(A)+1):
	sum_2 = sum_2 +i
print(sum_2 - sum_1)