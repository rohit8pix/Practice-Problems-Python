#USING split() method
string = "thank.you.very.much.rohit.roshan"

def reverse1(string):
	k =string.split(".")
	rev =k[::-1]
	temp=""
	for ele in rev:
		temp = temp+ele
		temp=temp+"."
	print(temp[:len(temp)-1])


# USING STACK

from collections import deque
def reverse2(s):
    l = h = 0
    stack = deque()
    for i, k in enumerate(s):
        if k == '.':
            stack.append(s[l:h + 1])
            l = h = i + 1
        else:
            h = i

    stack.append(s[l:])
    tmp = ""
    while stack:
        tmp += stack.pop() + "."
 
    return(tmp[:-1])     

print(reverse2(string))
reverse1(string)


#INPUT

# string = "thank.you.very.much.rohit.roshan"

#OUTPUT

# roshan.rohit.much.very.you.thank
