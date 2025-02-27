class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ### Observations
        # if there is no orange in the first place
        # we return -1 if there are still left over orange

        # Since its not gonna be one orange rotten all the way through
        # Sounds like a bfs
        # Init a queue storing all the rotten orange location
        rotten_orange = deque()

        # Init the total fresh orange count
        fresh_orange_count = 0

        # Iteration on the entire matrix
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # Updating the matrix, fresh orange count
                if grid[row][col] == 1:
                    fresh_orange_count += 1
                
                if grid[row][col] == 2:
                    rotten_orange.append((row, col))
                
        # If there is no fresh orange
        if fresh_orange_count == 0:
            return 0
        
        # Number of minutes taken init
        minutes = 0
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        # Perform bfs
        # While there is still rotten orange left
        # We can end early if fresh_orange_count reaches 0
        while rotten_orange and fresh_orange_count > 0:
            # Number of minutes taken update
            minutes += 1

            # Current layer of rotten orange
            for _  in range(len(rotten_orange)):
                # pop the rotten orange
                curr_rotten_orange = rotten_orange.popleft()
                curr_rotten_orange_row, curr_rotten_orange_col = curr_rotten_orange

                # if its surrounding is fresh orange, considering the bound, rot it
                for curr_dir in directions:
                    orange_check_row = curr_rotten_orange_row + curr_dir[0]
                    orange_check_col = curr_rotten_orange_col + curr_dir[1]
                    if orange_check_row >= 0 and orange_check_row < len(grid) and \
                        orange_check_col >= 0 and orange_check_col < len(grid[orange_check_row]) and \
                        grid[orange_check_row][orange_check_col] == 1:
                            # update fresh orange count 
                            grid[orange_check_row][orange_check_col] = 2
                            fresh_orange_count -= 1
                    
                            # add to the queue
                            rotten_orange.append((orange_check_row, orange_check_col))
            
        return minutes if fresh_orange_count == 0 else -1