'''
The key is to realize that we need to check for both side of the current position at which we are checking

I know, brute forcing it is fucking stupid but thats O(n)
'''
def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
	if (n == 0):
		 return True
	
	num_can_plant = 0
	curr_posn = 0
	
	while curr_posn < len(flowerbed):
		if (not flowerbed[curr_posn]) \
				and (curr_posn == 0 or not flowerbed[curr_posn - 1]) \
				and (curr_posn == len(flowerbed) - 1 or not flowerbed[curr_posn + 1]):
				num_can_plant += 1
				curr_posn += 1
		curr_posn += 1
		
	return n <= num_can_plant