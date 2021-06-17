color = "GGGGGGRGR"

def RedorGreen(color):
	r=0
	g=0
	for i in color:
		if i=='R':
			r+=1
		elif i=='G':
			g+=1

	print(min(r,g))