'''
A sliding window problem that does not require left/right index
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
