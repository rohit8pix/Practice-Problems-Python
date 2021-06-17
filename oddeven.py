#JPMORGAN HIREVUE @1
string = "66578982836454832450048"
num=[]
ans=[]
for ele in string:
	num.append(int(ele))

def numtype(x):
	if x%2==0:
		return 1
	else:
		return 0


if len(num)==0:print("NONE")
else:
	i=0
	while i!=len(num)-1:
		if numtype(num[i]) == 1 and numtype(num[i+1])==1:
			ans.append(num[i])
			ans.append("*")
		elif numtype(num[i])==0 and numtype(num[i+1])==0:
			ans.append(num[i])
			ans.append("-")
		else:
			ans.append(num[i])

		i=i+1
	ans.append(num[i])
	str1 = ''.join(str(e) for e in ans)
	print(str1)
