num1 = [2]
num2 = []

num1 = num1 +num2
num1.sort()

size = len(num1)
if size % 2!=0:
	x = int((size-1)/2)
	print(num1[x])
if size % 2==0:
	x = int((size-1)/2)
	print((num1[x]+num1[x+1])/2)

print(num1)