'''
The key is to sort the nums first and to do a for loop
'''
# Solution 1: sort it first
def maxOperations(nums: List[int], k: int) -> int:
	nums.sort()
	left = 0
	right = len(nums) - 1
	ret = 0
	
	while left < right:
		if nums[left] + nums[right] == k:
			ret = 0
			left += 1
			right -= 1
		elif nums[left] + nums[right] < k:
			left += 1
		else:
			right -= 1
			
		return ret

# Solution 2: Using hashmap, turned out to be slower
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_dict = Counter(nums)
        ret = 0
        for ele in nums:
            # for every element in nums, if there exist such a element
            # of (k - ele)
            # and at the same time the number of occurrence of this element is non-zero
            if (k - ele) in num_dict and num_dict[k - ele] != 0 and num_dict[ele] != 0:
                # if repeated element happens to be = k
                if (k - ele) == ele:
                    if num_dict[k - ele] >= 2:
                        # how many time can the occurrence of this element be divided by 2
                        nums_index = num_dict[ele] // 2
                        num_dict[k - ele] -= 2 * nums_index
                        ret += nums_index
                    else:
                        continue
                # if k - ele is not the same as ele
                else:
                    largest_minus = min(num_dict[k - ele], num_dict[ele])
                    num_dict[k - ele] -= largest_minus
                    num_dict[ele] -= largest_minus
                    ret += largest_minus

        return ret