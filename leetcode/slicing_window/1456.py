'''
A sliding window problem that does not require left/right index

Always think on every update of sliding window, can we process the newest element instead of the entire window, would be so much faster
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}  # Use a set for quick lookup
        
        # Count vowels in the first k-length window
        curr_vowel = sum(1 for i in range(k) if s[i] in vowels)
        max_vowel = curr_vowel  # Track max vowel count
        
        # Slide the window across the string
        for i in range(k, n):
            if s[i] in vowels:
                curr_vowel += 1  # Add new rightmost character
            if s[i - k] in vowels:
                curr_vowel -= 1  # Remove leftmost character
            max_vowel = max(max_vowel, curr_vowel)
        
        return max_vowel

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        aeiou = set("aeiou")
        curr = 0
        for i in range(0, k):
            if s[i] in aeiou:
                curr += 1
        ret_max = curr

        for i in range(len(s) - k):
            if s[i + k] in aeiou:
                curr += 1
            if s[i] in aeiou:
                curr -= 1
            ret_max = max(curr, ret_max)

        return ret_max