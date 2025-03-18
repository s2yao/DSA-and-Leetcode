class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # initial bottom most row
        row = [1] * n

        # iteration to process the rest of the rows
        for i in range(m - 1): # m - 1 since init row taken out
            newRow = [1] * n
            for j in reversed(range(n - 1)): # we leave out the right most index of the curren row on top of given row
                newRow[j] = newRow[j + 1] + row[j] # + right and + bottom
            row = newRow
        
        return row[0] # The top most element


                
