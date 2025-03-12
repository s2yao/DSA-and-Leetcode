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










sol = Solution()
nums = [2, 9, 5, 6, 2, 3, 3, 3, 9, 2]
print(sol.rob(nums))
print(len(nums))