'''
Using dp array to store the maximum from 0 to i - 1
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case len == 0
        if len(nums) == 0:
            return 0

        # Bottom up

        dp = [0] * (len(nums) + 1) 
        # dp[i] stores the current max of nums from 0 to i - 1
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(1, len(nums)): # decide whether we pick the current ith element
            dp[i + 1] = max(dp[i - 1] + nums[i], dp[i])
            # whether its the curr_max from 0 to i - 2 + nums[i]
            # Or we dont consider the current element      
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
            curr_max = max(curr_max, prev_max + num) # it uses i - 1, i, to make i + 1
            prev_max = temp
            # These magically makes 2 space apart from prev_max and curr_max
            # Since we initalized prev_max as the current max before change
        
        return curr_max










sol = Solution()
nums = [2, 9, 5, 6, 2, 3, 3, 3, 9, 2]
print(sol.rob(nums))
print(len(nums))