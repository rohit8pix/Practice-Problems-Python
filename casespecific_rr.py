inp1 = "eDefSR"
inp2 = "ghhhEEEkjGFHDO"

def casespecific(inp1):
	def uplow(inp1):
		upper = []
		lower = []
		for i in inp1:
			if i>='A' and i<='Z':
				upper.append(i)
			elif i>='a' and i<='z':
				lower.append(i)
		upper.sort()
		lower.sort()
		return(upper,lower)

	upper,lower =uplow(inp1)

	k=0
	j=0
	ans=[]
	for x in range(len(inp1)):
		if inp1[x]>='A' and inp1[x]<='Z':
			ans.append(upper[k])
			k+=1
		elif inp1[x]>='a' and inp1[x]<='z':
			ans.append(lower[j])
			j+=1

	temp = " "
	for x in ans:
		temp = temp+x
		
	return(temp)


print(casespecific(inp1))
print(casespecific(inp2))
