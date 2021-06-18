

def Balanced(num):
	st = str(num)
	if len(st)%2!=0:
		size = len(st)
		mid = int((size+1)/2)-1
		summ=0
		summ2=0
		for x in st[:mid]:
			summ =summ+int(x)
		for j in st[mid+1:]:
			summ2 = summ2+int(j)
	
		if summ == summ2:
			print("Balanced Number")
		else:
			print("Not a Balanced Number")

	else:print("error")
		
Balanced(1234006)
Balanced(1234)
