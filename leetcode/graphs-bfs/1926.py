'''
The key is to understand the "layer processing" of a bfs algorithm
And to set the beginning to be a wall right at the beginning

Initalization of directions
'''

from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        # The directions for movement (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # A queue for BFS, storing (row, col) and the current distance (layer)
        queue = deque([(entrance[0], entrance[1])])
        
        # Set the entrance as visited by marking it as a wall
        maze[entrance[0]][entrance[1]] = '+'
        
        # Recording the current minimum number of steps (layers)
        layers = 0

        while queue:
            layers += 1
            
            for _ in range(len(queue)):  # Iterate through the current layer
                curr_row, curr_col = queue.popleft()

                for u, v in directions:
                    curr_dir_row = curr_row + u
                    curr_dir_col = curr_col + v

                    # Check if the next position is within bounds
                    if (0 <= curr_dir_row < len(maze) and
                        0 <= curr_dir_col < len(maze[0]) and
                        maze[curr_dir_row][curr_dir_col] == "."):

                        # Check if the current position is an exit
                        # Since we are processing each element in each layer, so its possible that a lane is already at the final position
                        # But we if dont put the end condition here, its possible that we will return the layer of the first exit we find
                        # So we need to check if the current position is an exit, WITHIN THE LOOP
                        if maze[curr_dir_row][curr_dir_col] == "." and \
                            curr_dir_row == 0 or curr_dir_row == len(maze) - 1 or \
                            curr_dir_col == 0 or curr_dir_col == len(maze[curr_dir_row]) - 1:
                            return layers

                        # Mark the cell as visited and add to queue
                        maze[curr_dir_row][curr_dir_col] = "+"
                        queue.append((curr_dir_row, curr_dir_col))
        
        # If no exit is found
        return -1
