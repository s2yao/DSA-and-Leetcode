'''
Brute force, separate the sum and the final return value
'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ret = 0
        curr_alt = 0
        for i in range(len(gain)):
            curr_alt += gain[i]
            ret = max(ret, curr_alt)

        return ret
        