class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()  # O(m log m) - Sorting the potions
        m = len(potions)
        ret = []

        for spell in spells:  # O(n)
            # Minimum potion required to make the spell successful
            required_potion = (success + spell - 1) // spell  # Correct rounding

            # Binary search to find the first valid potion
            left = 0
            right = m - 1
            index = m  # Default case: no potion is valid

            while left <= right:  # O(log m)
                mid = (left + right) // 2
                if potions[mid] >= required_potion:
                    index = mid  # Store the first valid index
                    right = mid - 1  # Move left to find an even smaller valid index
                else:
                    left = mid + 1  # Move right to find a valid potion

            # The count of valid potions is everything from `index` to the end
            ret.append(m - index)

        return ret
