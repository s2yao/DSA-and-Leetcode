'''
The key is to keep track of the number of 1s on left side and on right side
Always remember the edge cases and their potential effects
'''
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ret = -1  # The final max length (must be updated whenever we hit 0)
        left_ct = 0  # Count of 1s before a 0
        right_ct = 0  # Count of 1s after a 0

        for i in range(n):
            if nums[i] == 1:
                right_ct += 1
            else:
                ret = max(ret, left_ct + right_ct)  # Update max length before resetting
                left_ct = right_ct  # Move right counter to left
                right_ct = 0  # Reset right counter

        # Handle the case when the last element is a 1
        ret = max(ret, left_ct + right_ct)

        # If `ret == n`, that means all elements were 1s, so we must remove one
        return ret - 1 if ret == n else ret
