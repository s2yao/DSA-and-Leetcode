'''
Fast and slow pointer
'''
def moveZeroes(nums):
    posn_to_write = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[posn_to_write]
            nums[posn_to_write] = nums[i]
            nums[i] = temp
            posn_to_write += 1
    
    return nums

nums = [0,1,0,3,12]

print(moveZeroes(nums))