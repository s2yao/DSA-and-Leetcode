'''
The key is to realize that we can split the total product to “left side” and “right side”.

Then we can have an array that records the prefix sum and suffix sum
'''
def productExceptSelf(nums: List[int]) -> List[int]:
	ret = []
	prefix = [nums[0]]
	suffix = [nums[-1]]
	
	# Putting the product of prefix[-1] * nums[i] into prefix
	for i in range(1, len(nums) - 1):
		prefix.append(nums[i] * prefix[-1])
		
	# Putting the product of suffix[-1] * nums[i] into suffix
	for i in range(len(nums) - 2, 0, -1):
		suffix.append(nums[i] * suffix[-1])
		
	for i in range(len(nums)):
		if i == 0:
			# The left more position of ret should be the product of all elements except for the first one
			ret.append(suffix[-1])
		elif i == len(nums) - 1:
			# Same logic
			ret.append(prefix[-1])
		else:
			# Multiply the prefix i - 1 posn with suffix len(suffix) - 1 - i
			ret.append(prefix[i - 1] * suffix[len(suffix) - 1 - i])
		return ret