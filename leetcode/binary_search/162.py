'''
The algorithm that was used in the array/string
Use a minimum value and only check one side of the list
If there is any value that doesnt meet a set requirement, we can decide a value need to be return
'''
class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return i - 1
        return len(nums) - 1