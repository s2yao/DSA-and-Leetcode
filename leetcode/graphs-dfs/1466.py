'''
This problem requires a dfs search starting from city 0

We alter the data structure to perform this dfs
- by making a undirected graph using dictionary

The initialize of directed and undirect graph
'''

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
        # We need a dfs starting from city 0
        # But the edge is not in the right direction to go in depth

        # We make a undirected graph, and we store the directed graph for comparisons
        # of "misdirections"

        # Set to store the directed graph
        directed = {(a, b) for a, b in connections}

        # Dictionary to store the undirected graph
        undirected = defaultdict(list)
        for a, b in connections:
            undirected[a].append(b)
            undirected[b].append(a)
            
        # set to make sure no city appeared twice
        visited_city = set([0])

        # A stack for dfs
        stack = [0]

        ret = 0

        while stack:
            # Get the current city from stack
            curr_city = stack.pop()

            # An iteration to find all the neighbor of current city
            for neighbor in undirected[curr_city]:

                # if the current neighbor existed in the visited_set
                if neighbor in visited_city:
                    # We continue
                    continue
                
                # if current direction not in the directed graph set
                if (neighbor, curr_city) not in directed:
                    # The current direction is wrong
                    ret += 1

                visited_city.add(neighbor)
                stack.append(neighbor)
            
        return ret
            
