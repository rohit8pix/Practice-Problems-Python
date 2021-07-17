string = "helloworld"
def half_iter_rohit(string):
	"""O(n) time it takes due to adding the elements of res"""
	"""soln by ROHIT ROSHAN"""
	start=0
	end=len(string)-1
	res  = [0]*len(string)
	while start<=end:
		res[start], res[end] = string[end], string[start]
		start+=1
		end-=1

	string = ""
	for i in res:
		string+=i
	print(string)

def half_iter_pratik(string):
	"""n/2 iteration"""
	"""Soln by PRATIK RAJ"""
	right=len(string)-1
	mid=len(string)//2
	str1=""
	str2=""
	for i in range(mid):
		str1+=string[right-i]
		str2+=string[mid-1-i]
	if len(string)%2==0:
		print(str1+str2)
	else:
		print(str1+string[mid]+str2)







