def dupli(input_string):
	st = set()
	strng =""
	for i in input_string:
		if i not in st:
			strng=strng+i
			st.add(i)
		else:
			pass
	return(strng)

print(dupli('rrhhii'))

