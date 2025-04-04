'''
The key is to know how to iterate digit by digit -- & 1
>>= syntax
'''
class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ret = 0
        while a or b or c: # while a, b, c hasnt run out
            abit = a & 1
            bbit = b & 1
            cbit = c & 1
        
            if abit == 1 and bbit == 1 and cbit == 0:
                ret += 2
            else:
                if abit | bbit != cbit:
                    ret += 1
                
            a >>= 1
            b >>= 1
            c >>= 1
        
        return ret