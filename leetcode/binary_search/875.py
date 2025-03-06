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
        left = 0
        right = len(piles) - 1

        while left <= right:
            curr_speed = (left + right) // 2
            # what is the time taken to finish all the piles
            time_taken = sum((pile + curr_speed - 1) // curr_speed for pile in piles)

            if time_taken > h: # if the time taken is too long, we increase the speed
                left = curr_speed + 1
            else:
                right = curr_speed - 1

        return left

lst = [30,11,23,4,20]
guess = 15
print([(element + guess - 1) // guess for element in lst])