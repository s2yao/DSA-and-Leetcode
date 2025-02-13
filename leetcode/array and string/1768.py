'''
The key is to understand string slicing
'''
def mergeAlternately(word1: str, word2: str) -> str:
	ret = ""
	n = min(len(word1), len(word2))
	
	for i in range(n):
		ret += word1[i] + word2[i]

	if (len(word1) == len(word2))
		return ret
	if (len(word1) > len(word2)):
		ret += word1[n:]
	else:
		ret += word2[n:]
	return ret