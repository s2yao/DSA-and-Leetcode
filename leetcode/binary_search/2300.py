'''
The algorithm of performing binary search all the way
    Note that it is better to have another "result" value to record down the "cutoff"
'''
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        # Since we need to find all the potions that works
        # and potion multiplies the current spell
        # We can caluclate the cutoff of the potions

        potions.sort()
        ret = []

        for spell in spells:
            required_potion = (spell + success - 1) // spell # how many times we need to add spell to make result >= success

            # We find the first potion that fits the requirement
            left = 0
            right = len(potions) - 1
            cutoff = len(potions) # init to the default case, since if there is no valid potion, we need to put 0
            while left <= right:
                curr_guess = (left + right) // 2
                if potions[curr_guess] >= required_potion:
                    right = curr_guess - 1
                    cutoff = curr_guess
                else:
                    left = curr_guess + 1

            ret.append(len(potions) - cutoff)  
        return ret