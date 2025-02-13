'''
Use a stack
'''
class Solution:
    def removeStars(self, s: str) -> str:
        
        ret = []

        for element in s:
            if element == '*':
                if len(ret) != 0:
                    ret.pop(-1)
            else:
                ret.append(element)
        
        return ''.join(ret)