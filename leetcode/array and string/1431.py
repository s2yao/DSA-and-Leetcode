'''
Literally no point
'''
def fuck(candies: List[int], extra: n) -> List[int]:
	ret = []
		
	max_ele = max(candies)
	
	for i in range(len(candies)):
		if n + candies[i] >= max_ele:
			ret[i].append(True)
		else:
			ret[i].append(False)