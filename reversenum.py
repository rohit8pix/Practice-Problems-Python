'''class Solution:
def reverse(self, x: int) -> int:
    sign, out = -1 if x < 0 else 1, int(str(abs(x))[::-1])
    return out * sign if -(2**31) < out < 2**31 else 0'''
    
        

        
        
        
        


def reverse(x):
    if x >= 2**31-1 or x <= -2**31: return 0
    else:
        strg = str(x)
        if x >= 0 :
            revst = strg[::-1]
        else:
            strg = str(-1234)
            revst = (("-"+strg[1:][::-1]))
        if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
        else: return revst

print(reverse(120))
      
