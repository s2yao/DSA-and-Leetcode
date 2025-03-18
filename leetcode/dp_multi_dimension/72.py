'''
First 2D DP problem that i have solved

The key is to realize that the right, down, right-down correspond to delete, replace, and insert

And that if 2 element equals, we just skip to next character for both word1 and 2

The "set up" of the problem
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]

        for i in range(len(word1) + 1):
            dp[len(word2)][i] = len(word1) - i

        for j in range(len(word2) + 1):
            dp[j][len(word1)] = len(word2) - j


        for i in reversed(len(word1)): # (len(word1) - 1) to 0
            for j in reversed(len(word2)):
                if word1[i] == word2[j]:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])

        return dp[0][0]