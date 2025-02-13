'''
It extremely important to realize that with out an equal sign, 
the second could be replaced by the same value as the first, 
where if theres a smaller value and bigger value, would return True
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False

        # Initialize two pointers with infinities
        first = float('inf')
        second = float('inf')

        for i in nums:
            # consider the case when 1 1 2
            if i <= first:
                first = i
            # consider the case when 1 2 2
            # we have to make sure the same number does not "slip" onto the next level
            elif i <= second:
                second = i
            else:
                return True
        
        return False