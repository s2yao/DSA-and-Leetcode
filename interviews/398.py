import random
# Google

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = nums
        self.dict = defaultdict(lambda: [0, []])
        for i in range(len(nums)):
            self.dict[nums[i]][0] += 1
            self.dict[nums[i]][1].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        # BC: target DNE return Null
        if self.dict[target][0] == 0:
            return None
        
        # curr_random will be between 0 to (curr_random - 1)
        curr_random = random.randint(0, self.dict[target][0] - 1)
        
        return self.dict[target][1][curr_random]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)