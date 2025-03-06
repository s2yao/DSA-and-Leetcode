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
            if nums[i - 1] > nums[i]:
                return i

        return len(nums) - 1


# This second solution uses binary search
# And it uses "right" as the anchor for the current found peak
# Uses left to potentially finding more peak
# Or to shrink the bound
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1 # because we are checking current element and current + 1 element

        # We are searching for the element, every time we find a element that fits we use right to record it
        # If left ever == right, that mean the element originally sitting at left is smaller than right
        while left < right:
            curr_guess = (left + right) // 2

            if nums[curr_guess] > nums[curr_guess + 1]:
                right = mid
            else:
                left = mid + 1

        return right