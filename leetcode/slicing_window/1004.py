'''
The key is to know the concept of “owing” number of flips, and to maintain the size of the maximum consecutive 1s, if we are on the “owing” state.
Let k be the amount of flips we have, and that it can be negative.
'''
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0

        for right in range(len(nums)):
            # When we encounter a 0, we use one flip
            if nums[right] == 0:
                k -= 1

            # If k goes negative, move left pointer to restore balance
            while k < 0:
                if nums[left] == 0:
                    k += 1  # We "give back" a flip
                left += 1  # Shrink window

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len
