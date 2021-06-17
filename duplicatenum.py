def removeDuplicates(nums): 
    count=0
    j=1
    for j in range(0,len(nums)):
        if nums[j]!=nums[count]:
            count+=1
            nums[count]=nums[j]
                
    return count+1
        
num=[1,1,2,3,4]
removeDuplicates(num)
print(num)