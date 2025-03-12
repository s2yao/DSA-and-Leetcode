'''
Intro to DP
We store some of the results in an array
Sacrificing space for efficiency
'''
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        arr = [0] * (n + 1)
        arr[0] = 1
        arr[1] = 1
        arr[2] = 2

        for i in range(3, n):
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
        
        return arr[n-1]