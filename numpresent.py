#learn about set

x =[]
num=[1,1,2,4,6,8,8,9]
for i in num:
    if i not in x:
        x.append(i)
x.sort(reverse=True)
print(x)

if len(num)>=3 and len(x)>=3:
    print(x[2])
elif len(num)==2:
    print(x[0])
elif len(x)==1:
    print(x[0])
elif len(num)>=3 and len(x)==2:
    print(x[0])



## good solution

'''arr = list(set(num))
arr.sort()
print(arr)
if len(arr)>=3:
    print(arr[-3])
else:
    print(arr[-1])'''

print(set(num))




















'''def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set()
        # add all numbers to a set. sets do not allow duplicate entries so this will take care of that issue itself
        for i in nums:
            numset.add(i)

        #make a list so we can order and access the numbers
        lst = list(numset)
        lst.sort()

        # "if the third maximum does not exist, the maximum is returned instead."
        if len(lst) >= 3:
            return lst[-3]
        else:
            return max(lst)'''
