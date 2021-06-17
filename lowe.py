A=[5,30,10,7]
even = []
odd =[]
even_1=[]
for ele in A:
	if ele%2==0 and ele%5==0:
		even.append(ele)
	elif ele%2==0 and ele%5!=0:
		even_1.append(ele)
	else:
		odd.append(ele)

ans = dict()
idx=[]
for i in range(len(A)):
	if A[i]%5!=0:
		ans[i]=A[i]
	if A[i]==5:
		ans[i]=A[i]

k=list(ans.keys())
k.sort(reverse=True)

notdiv =[]
for element in k:
	notdiv.append(ans[element])

div_5 =[]
for i in range(len(even)):
	if even[i]%5==0:
		div_5.append(even[i])
div_5.sort(reverse=True)


if sorted(notdiv)!=sorted(odd):
	div_5.extend(even_1)
	div_5.extend(odd)
else:
	div_5.extend(odd)

print(div_5)

