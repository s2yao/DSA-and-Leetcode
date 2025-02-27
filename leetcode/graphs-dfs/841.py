'''
Understand the graph dfs/bfs algorithm
'''

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        stack = rooms[0]
        visited_set = set([0])

        while stack:
            curr_node = stack.pop()
            if curr_node not in visited_set:
                visited_set.add(curr_node)
                for room in rooms[curr_node]:
                    if room not in visited_set:
                        stack.append(room)

        return len(visited_set) == len(rooms)