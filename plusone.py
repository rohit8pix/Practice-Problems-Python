list1 = [1,4]
str1 = ''.join(str(e) for e in list1)

num = int(str1)
num=num+1
res = [int(x) for x in str(num)]
print(num)