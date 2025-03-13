'''
Using dp array to store the maximum from 0 to i - 1
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Bottom up approach
        if len(nums) == 0:
            return 0

        # This dp array stores the maximum money possible from idx 0 to i - 1
        dp = [0] * len(nums) + 1
        dp[0] = 0
        dp[1] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i - 1] + nums[i], dp[i])
        
        return dp[-1]

'''
It seems like we only need to record:
The current maximum
The prev maximum

and if current maximum is > prev + current number

we replace the curr_max with prev + current num
'''
    def rob2(self, nums):
        if len(nums) == 0:
            return 0
        
        curr_max = 0
        prev_max = 0

        for num in nums:
            temp = curr_max
            curr_max = max(curr_max, prev_max + num)
            prev_max = temp
        
        return curr_max










sol = Solution()
nums = [2, 9, 5, 6, 2, 3, 3, 3, 9, 2]
print(sol.rob(nums))
print(len(nums))