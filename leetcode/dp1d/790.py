'''
The key is to come up with this "<number of pattern> x n" thats calculating along with the given 2 x n
    A for loop on each index
    Using different "states" for each pattern
Initializing a ?D array using for loop
'''
class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        # We first initalize a dp
        # We make a 4 x n
        # It will record all the different state
        dp = [[-1] * 4 for _ in range(n + 1)]

        # The function that classifies the states
        # There will only be 4 states
        def state(t1, t2):
            if not t1 and not t2:
                return 0
            elif t1 and t2:
                return 1
            elif t1 and not t2:
                return 2
            else:
                return 3

        def solving(col, t1, t2):
            if col == n:
                return 1 # The base case as there is only one way that we can reach the end from n-1
            curr_state = state(t1, t2) # Return the current classified state
            if dp[col][curr_state] != -1:
                # if we have visited this state before
                return dp[col][curr_state]
            t3 = (col + 1 < n)
            t4 = (col + 1 < n)
            count = 0
            # All the possible block placing
            if (t1 and t2 and t3): count += solving(col + 1, False, True) # next iteration only t2 available
            if (t1 and t2 and t4): count += solving(col + 1, True, False) # only t1 available
            if (t1 and not t2 and t3 and t4): count += solving(col + 1, False, False) # 刚刚好放进去3
            if (not t1 and t2 and t3 and t4): count += solving(col + 1, False, False) # 刚刚好放进去3
            if (t1 and t2): count += solving(col + 1, True, True) # 竖着放2
            if (t1 and t2 and t3 and t4): count += solving(col + 1, False, False) # 横着放两个2
            if (t1 and not t2 and t3): count += solving(col + 1, False, True) # 横着放一个2, 1
            if (not t1 and t2 and t4): count += solving(col + 1, True, False) # 横着放一个2, 2
            if (not t1 and not t2): count += solving(col + 1, True, True) # 目前t1, t2都满了
            # We have process everything from the col
            # and that we can record it in the dp, and to remember it
            dp[col][curr_state] = count
            return count

        return solving(0, True, True) % (10 ** 9 + 7)