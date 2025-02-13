'''
The key is to keep track of the last repeated character (left) of the current character (right)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        left = 0
        right = 0
        set_char = set()

        while right < len(s):
            if s[right] in set_char:
                # bring the last repeated character into its correct position
                while s[left] != s[right]:
                    set_char.discard(s[left])
                    left += 1
                left += 1
            else:
                set_char.add(s[right])
                ret = max(ret, right - left + 1)
            right += 1
        # at this point we iterate through the entire array
        return ret