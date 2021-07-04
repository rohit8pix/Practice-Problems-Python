import math
# have to check for bugs and optimize the solution
n = 2
vac_Type = [8]

def findnonzero(arr):
	i=0
	while arr[i]==0:
		i=i+1
	return(i+1)


if len(vac_Type)>=1 and (vac_Type[0]%n)!=0 and n>=len(vac_Type):
	deal = [0]*n 
	for i in range(len(vac_Type)):
		deal[i]=vac_Type[i]
	deal.sort()


	length = findnonzero(deal)
	for i in range(length):
		index = deal.index(max(deal))
		if deal[i]==0:
			k=math.ceil(max(deal)/2)
			deal[i]=k
			deal[index] = deal[index]-k
	print(max(deal), deal)


elif len(vac_Type)==1:
	ans = [vac_Type[0]//n]*n
	print(ans)
	 
else:
	res = sorted(vac_Type)
	print(res[:n])
