'''
The key is to realize that, in order to get the final occurrences of each distinct element in “arr”, 
its necessary for us to do a full traversal to record each element and number of time appearing

Sounds like a dictionary

A lot of dictionary syntax
'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        # dict that pairs corresponding elements and their occurrence
        arr_dict = dict()
        
        # full traversal
        for item in arr:
            if item not in arr_dict:
                arr_dict[item] = 1
            else:
                arr_dict[item] += 1
			   
        unique_set = set()
			  
        for key in arr_dict:
            if arr_dict[key] in unique_set:  # Check the occurrence count, not the key itself
                return False
            else:
                unique_set.add(arr_dict[key])
				
        return True
