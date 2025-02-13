'''
The key is to start from both side with left, right indexes, 
and that the higher the left and right bar is, 
the better chance that the container area be the largest
'''
def maxArea(height):
    left = 0
    right = len(height) - 1
    ret = 0

    while left < right:
        curr_area = (right - left) * min(height[left], height[right])
        ret = max(ret, curr_area)
        if (height[left] < height[right]):
            left += 1
        elif (height[left] > height[right]):
            right -= 1
        else:
            left += 1
            right -= 1
    
    return ret


height = [1,1]
print(maxArea(height))