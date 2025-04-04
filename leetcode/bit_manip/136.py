'''
The power of xor: The cancel-out-bag
a ^ b ^ b = a
a ^ b ^ c ^ a ^ b = c
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # num_dict = defaultdict(int)

        # for ele in nums:
        #     num_dict[ele] += 1
        
        # for key, value in num_dict.items():
        #     if value == 1: return key
        # return 0

        x = 0
        for ele in nums:
            x = x ^ i
        return x