'''
Stupid question
'''
def isSubsequence(s: str, t: str) -> str:
	if len(s) > len(t):
	  return False
	if len(s) = "":
		return True
		
	curr_index = 0
	for i in range(len(t)):
		if t[i] == s[curr_index]:
			curr_index += 1
		
		if curr_index == len(s):
			return True
	return False
	