class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) < 2:
            return cost[0]
        # Building an array, and for ith position records the minimum cost to get to ith position
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(dp)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        return min(dp[-1], dp[-2])