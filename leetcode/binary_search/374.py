'''
Binary search
'''
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0 
        right = n

        while left <= right:
            mid = (right + left) // 2
            curr_guess = guess(mid)
            if curr_guess == 0: # correct
                return mid
            elif curr_guess == -1: # supposed to be belong
                right = mid - 1
            else:
                left = mid + 1
        
        return -1