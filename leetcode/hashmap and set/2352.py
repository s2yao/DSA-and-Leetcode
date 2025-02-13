'''
My initial attempt is to put every rows and cols into a set, while appending each integer into a single string

The correct solution to this problem requires understanding of the following methods:
* — unpacking operator

zip() — takes the ith index until i reaches the end, and combine each element given’s ith position to form a tuple

- This returns a iterator

map() — maps a function into a iterable object

Counter() — Only takes iterable and hashable (unmutatable) object, outputs a “dictionary” (Counter object)

- note that accessing a non-existent key for the output of a counter function returns 0
- where a dictionary will just output error
'''
class Solution:                                
    def equalPairs(self, grid: List[List[int]]) -> int:
    
	    # We make a Counter typed "dict" by unpacking the list of list of int
	    # into bunch of lists of int
	    # then we use zip's characteristic to get the exact transpose, which
	    # outputs a "iterator of tuple"
	    # The requirement for Counter is that it should be, 1. iterable, 2. hashable (unmutatable)
	    transpose = Counter(zip(*grid))
	    
	    # maps tuple function into each list of int to let them become tuple of
	    # int, which is also an "iterator of tuple"
	    # Which statisfies the requirement for Counter
	    grid = Counter(map(tuple, grid))
	    
	    # Returns the sum of all products of the occurrences of intersecting keys
		  # Note that for a dictionary, accessing the value from a non-existent key outputs error
		  # But for Counter "dictionary" (counter object), accessing a non-existent element returns 0, so this works
	    return sum(transpose[i] * grid[i] for i in transpose)
	    