'''
The key is to realize that we need to check for both side of the current position at which we are checking

I know, brute forcing it is fucking stupid but thats O(n)

Always remember to consider based cases
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



class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if (n == 0):
            return True
            
        for i in range(len(flowerbed)):
            if i == 0 and len(flowerbed) >= 2:
                if flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1 and len(flowerbed) >= 2:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif len(flowerbed) == 1:
                return flowerbed[i] == 0
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1

        return n <= 0