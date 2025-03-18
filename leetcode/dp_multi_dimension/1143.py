'''
It is a template of doing a 2D DP problem
Where we use a "positional" storing technique in the 2D array
    One extra space for x and y for this 2D

Mind the x and y for the initialized array, and their order of accessing
    the lookup x y and the 2D array x y must match (prevent one being x y and other one being y x)

the xy position records the current progress of text1 and text2 for comparison
'''
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]


text1 = "abcde"
text2 = "ace" 
sol = Solution()
print(sol.longestCommonSubsequence(text1, text2))