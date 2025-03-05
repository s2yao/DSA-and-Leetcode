import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # pile[i] is ith pile of banana
        # h is number hours guard gone
        # return the eats per hour for koko

        # Brute force

        # init the return value as 1 since thats the least we can do
        # we increment this hour by 1 every time when the hours needed for eating a pile banana
        eat_per_hour = 1

        # Init a variable that records the current hour needed
        hour_taken = 0
        while hour_taken != h: # While the current eat_per_hour is not enough
            hour_taken = 0
            # An iteration through the current pile
            for pile in piles
                # Get the number of hour needed to finish the current pile
                '''
                what the fuck
                '''
                hours_needed = (eat_per_hour + pile - 1) // eat_per_hour
                # add it into the eat_per_hour
                hour_taken += hours_needed
        
        # if the loop has finished, it means we found the minimum eat_per_hour for given h
        return eat_per_hour