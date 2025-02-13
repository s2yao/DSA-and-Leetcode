from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        
        # Initialize window sum with the first k elements
        curr_sum = sum(nums[:k])
        max_sum = curr_sum  # Track max sum
        
        # Slide the window across the array
        for i in range(k, n):
            curr_sum += nums[i] - nums[i - k]  # Remove leftmost, add rightmost
            max_sum = max(max_sum, curr_sum)
        
        return max_sum / k  # Return max average
