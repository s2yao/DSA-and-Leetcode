'''
Standard backtrack algorithms
Each of the parameters:
index: for the current index of the digit that we need to process
progress: the current progress
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []

        letter_dict = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

        ret = []

        def backtrack(index, path):
            if index == len(digits):
                ret.append("".join(path))
                return
            
            for letter in letter_dict[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        
        backtrack(0, [])
        return ret

sol = Solution()
digits = "23459994"
print(sol.letterCombinations(digits))