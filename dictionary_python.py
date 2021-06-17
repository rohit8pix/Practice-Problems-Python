from collections import defaultdict
temp = defaultdict(list)
stringList = ["eat","tea","ate","bat","tab","rohit","tihor","tan","nat"]
for element in stringList:
    ##print(element)
    #print(temp)
    temp[str(sorted(element))].append(element)
    #print(str(sorted(element)))
print(temp)