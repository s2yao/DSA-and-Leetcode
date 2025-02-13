'''
The key is to have 2 index counting the 2 position that need to be swapped
An to remember that string is not mutable
'''
def reverseVowels(s: str) -> str:
	set_vowel = ("aeiouAEIOU")

	front, back = 0, len(s) - 1

	lst = list(s)
	# while a non repetitive swap is still possible
	while front < back:
		if lst[front] in set_vowel and lst[back] in set_vowel:
			temp = lst[front]
			lst[front] = lst[back]
			lst[back] = temp
			# remember the manually update the front and back to look for the next potential swap
			front += 1
			end -= 1

		if lst[front] not in set_vowel:
			front += 1

		if lst[back] not in set_vowel:
			back -= 1

	return "".join(lst)
