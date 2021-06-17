height = [1,8,6,2,5,4,8,3,7]
#def maxarea(height):
maxarea = 0
for i in range(0, len(height)):
	for j in range(i+1, len(height)):
		if height[i]<height[j]:
			area = height[i]*(j-i)
			#print(area,i,j)
		elif height[i]>=height[j]:
			area = height[j]*(j-i)
			#print(area,i,j)
		if area >= maxarea:
			maxarea = area
print(maxarea)


