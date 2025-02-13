'''
Operation 1: Single index swap

Operation 2: Single character change

In essence:

Operation 1: If the 2 elements on the 2 index that are swapping both have 1 occurrence in word1 and word2

Operation 2: If the 2 element to be interchanged have corresponding occurrence in both word1 and word2

Then for word1 and word2 **If number of distinct characters with occurrences of 1 is same, and the number of occurrences of other characters ends up being the same, then word1 is close to word2**

And its important to realize that the characters at which word1 and word2 has must be the same
'''
# Notice the use of index sorting
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
	    letter1 = [0] * 26
	    letter2 = [0] * 26
	    
	    for element in word1:
		    letter1[ord(element) - ord('a')] += 1
		  
	    for element in word2:
		    letter2 [ord(element) - ord('a')] += 1
		  
		  # check if either word1 or word2 have different characters
		  for i in range(26):
			  if ((letter1[i] == 0 and letter2[i] != 0) and (letter2[i] == 0 and letter1[i] != 0)):
			  return Fzalse
		  
		  letter1.sort()
		  letter2.sort()
		  
		  for i in range(26):
			  if letter1[i] != letter2[i]:
				  return False
			
			return True