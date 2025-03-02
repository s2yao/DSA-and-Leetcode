'''
Layer processing of bfs algorithm

Initalization of directions
'''
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # We need to keep track of the total number of orange
        total_oranges_count = 0
        # We need to keep track of the number of rotten orange
        rotten_orange_count = 0

        # A queue that stores only rotten oranges
        rotten_orange = deque() # stores tuple of (row, col)

        for row in len(grid):
            for col in len(grid[row]):
                # if orange is rotten, 
                if grid[row][col] == 2:
                    # store it into the queue
                    rotten_orange.append((row, col))
                    # update number of rotten orange
                    rotten_orange_count += 1

                # if orange is fresh or rotten, increment the total number of orange
                if grid[row][col] != 0:
                    total_oranges_count += 1
        
        if total_oranges_count == rotten_orange: # no fresh orange
            return 0

        # Now we have total orange count
        # and location of rotten oranges

        # init minutes
        minutes = 0

        # init directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue and total_oranges_count > 0:
            # if there are still rotten oranges and fresh oranges in this cycle
            # increment the minutes
            minutes += 1

            # iteration through the entire layer of rotten oranges
            for _ in range(len(rotten_orange))
                # get the leftmost element
                curr_orange_row, curr_orange_col = rotten_orange.popleft()

                # for 4 directions
                for u, v in directions:
                    # if curr_orange is not rotten
                    curr_dir_row = curr_orange_row + u
                    curr_dir_col = curr_orange_col + v
                    if grid[curr_dir_row][curr_dir_col] != 2:
                        rotten_orange_count += 1
                        grid[curr_orange_row + u][curr_orange_col + v] = 2 # Curr dir orange becomes rotten
                        rotten_orange.append([curr_orange_row + u], [curr_orange_col + v]) 
        
        if rotten_orange_count != total_oranges_count:
            return -1
        return minutes