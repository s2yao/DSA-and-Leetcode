from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Create an undirected graph with weighted edges
        adj = defaultdict(list)

        # Build the graph
        for i, (num, denom) in enumerate(equations):
            adj[num].append((denom, values[i]))
            adj[denom].append((num, 1 / values[i]))
        
        # Function to calculate the path using BFS
        def calculate_path(start, end):
            # Edge case: if either variable is not in the graph
            if start not in adj or end not in adj:
                return -1.0
            
            # BFS setup
            visited_set = set()
            queue = deque([(start, 1.0)])  # Store (current_node, cumulative_product)

            while queue:
                curr_node, curr_val = queue.popleft()

                # Mark the node as visited
                visited_set.add(curr_node)

                # Check if we've reached the target node
                if curr_node == end:
                    return curr_val
                
                # Explore neighbors
                for neighbor, weight in adj[curr_node]:
                    if neighbor not in visited_set:
                        queue.append((neighbor, curr_val * weight))
            
            # If no path found
            return -1.0
        
        # Evaluate each query
        ret = []
        for query in queries:
            ret.append(calculate_path(query[0], query[1]))
        
        return ret
