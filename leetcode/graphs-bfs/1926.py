class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        # im thinking to find all the possible route and figure out the best one

        # Recording the current minimum number of step
        layers = 0

        # the directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # a queue for bfs
        # stores list recording current element and current path
        queue = deque((entrance[0], entrance[1]))

        while queue: 
            layers += 1
            for _ in range(len(queue)): # Iterations on the current layer
                curr_row, curr_col = queue.popleft() 

                for u, v in directions:
                    curr_dir_row = curr_row + u
                    curr_dir_col = curr_col + v

                    # If this current direction is out of bound, we found an exit
                    if curr_dir_col == 0 or \
                        curr_dir_col == len(maze[curr_dir_row]) - 1 or \
                        curr_dir_row == 0 or \
                        curr_dir_row == len(maze[curr_dir_row]) - 1
                            return curr_ret

                    # If not yet an exit, we check if this one is a wall
                    if maze[curr_dir_row][curr_dir_col] != "+": # Current direction of the popped element is not wall
                        queue.append((curr_dir_row, curr_dir_col))
        
        return -1
        





        





        