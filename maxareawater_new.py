


height = [1,2,9,4,5]

def maxArea(height):
     
        left = 0
        right = len(height) - 1 #save index
        result = 0
        
        
        while left != right:
            h = min(height[left], height[right])
            area = (right - left) * h
            result = max(result, area) 
            
            if height[left] < height[right]:
                left = left + 1
            else: 
                right = right - 1 
                
        
        return result

print(maxArea(height))