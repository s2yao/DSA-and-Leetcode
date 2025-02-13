'''
The key is to realize if putting an array of element into a set, the set will contain each distinct elements in the array

Then we iterate through the set
'''
class Solution {
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
		# putting the given array in a set
		set1 = set(nums1)
		set2 = set(nums2)
		ret1 = []
		ret2 = []
		
		for element in set1:
			if element not in set2:
				ret1.add(element)
		
		for element in set2:
			if element not in set1:
				ret2.add(element)				

		return [ret1, ret2]
}