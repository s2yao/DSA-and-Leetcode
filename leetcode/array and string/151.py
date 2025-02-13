'''
The key to this problem is to realize that, if theres a built-in function in python, use it
1. split “splits” an string into an array of elements, where each element are separated by the keyword in side the (), space is filled if no parameter given
2. strip, “strips” the clothes of a string according to given parameter in (), and space is filled if no parameter is given
3. [::-1] reverses the array
'''
def reverseWords(s: str) -> str:
	arr = s.split()
	return " ".join(arr[::-1])

# Do this fucking problem not using built-in function
