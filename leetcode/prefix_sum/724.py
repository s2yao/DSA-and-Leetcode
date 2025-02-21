'''
The key is to calculate the sum of the array before and after i, where we compare the sum before and after i

Note that comparing the sum of the array before and after i using 2 pointer doesnt work, since the case where i sits at exactly 0 or len(nums) - 1 does not work
'''
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sum_all = sum(nums)

        pivot = 0
        for i in range(len(nums)):
            if pivot == sum_all - nums[i] - pivot:
                return i
            pivot += nums[i]

        return -1