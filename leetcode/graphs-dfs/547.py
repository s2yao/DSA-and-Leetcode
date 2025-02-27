'''
This is a dfs but in a for loop
DFS needs to be done to every single element of given array
'''

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # Look for province
        # no city --  0 province
        if isConnected == []:
            return 0
        
        # Set to avoid revisit
        visited_set = set()

        # init province count
        province_count = 0

        # we perform a dfs for every single city
        for curr_city in range(len(isConnected)):
            
            # if the curr_city is not visited, we perform a dfs search
            if curr_city not in visited_set:

                # stack for dfs
                stack = [curr_city]

                # while stack is not empty, we keep looking for its neighbors and add them into the stack
                while stack:

                    # get the current city from the stack
                    curr_city_dfs = stack.pop()

                    # update the current city into the visited_set
                    visited_set.add(curr_city_dfs)

                    # append all curr_city's neighbors into the stack
                    for neighbor in range(len(isConnected[curr_city])):
                        if neighbor not in visited_set and isConnected[curr_city][neighbor] == 1: # if this city has not been processed in this iteration and its connected to the curr_city_stack
                            stack.append(neighbor)

                # after stack empty, we have found a province
                province_count += 1
            
        return province_count





