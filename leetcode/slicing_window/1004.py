'''
For sliding window, we always need to consider the process of the newly added right element and the lastly added left element

This question records the length by right - left

If youre taking one index and minus it by another, result will be the elements between them + 1
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ret = 0
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] == 0:
                k -= 1
            if k < 0: # if k is not enough
                ret = max(ret, right - left)
                if nums[left] == 0:
                    k += 1
                left += 1
            right += 1
        ret = max(ret, right - left)
        return ret