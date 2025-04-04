'''
Genius
The number of 1s of the current number can be split into
curr_num >> 1 -- the number of 1s excluding the latest bit
+ 
curr_num & 1 -- whether the latest bit is a 1
'''
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp