'''
The key is to realize that if the largest string x can divide both s and t, then s + t can also be divided by x
and to also realize that the GCD of the length of 2 strings will be the exact length of the x
'''
import math
def gcdOfStrings(str1: str, str2: str) -> str:
	if (str1 + str2) != (str2 + str1):
		return ""
	
	gcd = math.gcd(len(str1), len(str2))
	
	return str1[:gcd]