'''
what the fuck: hours_needed = (eat_per_hour + pile - 1) // eat_per_hour

Whenever we are doing binary search
1. we think about the upper and lower bound of the search
2. when updating the bound, use brain to analyse
    its possible that the condition is different than the "mid"
3. If we do binary search "all the way", the minimum value in the array that fits the requirement will be sitting at "low"
4. everyone says that "binary search needs to be using to a sorted data"
    Think whether the current data is "sorted"
'''
class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)

        while low <= high:
            speed_guess = (low + high) // 2
            # how many hours current eating speed is needed to finish banana
            curr_hour = sum((pile + speed_guess - 1) // speed_guess for pile in piles)

            if curr_hour > h:
                # the current speed is too low
                low = speed_guess + 1
            else:
                high = speed_guess - 1
        
        return low
        
        return low