def isSub(s,t):
    for i, c in enumerate(s):
        if c not in t:
            return False
        p = t.index(c)
        if p == len(t) - 1 and i != len(s) - 1:
            return False
        t = t[p + 1 :]     
    return True


string1 =["GGTTGGGATTATCUCTAAATGTGA"] #VIRUS GENOME
string2 ="GGTTGGGATTTAGCTATCCTAAATGTGATGAAAATGCGTAAGTAGCUGTACTAGGACCAYCGTCGACCGTA" 

if len(string1)==0:
    print("NEGATIVE")
elif len(string1)!=0 and "" not in string1:
    for i in range(len(string1)):
        if isSub(string1[i], string2) and string1[i]!=0:
            print(string1[0],"virus is a derivative of", string2)
        else:
            print("NEGATIVE")
else:
    print("NEGATIVE")

    