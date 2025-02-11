from collections import deque

class Solution(object):
    def predictPartyVictory(senate):
        red = deque()
        dire = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                red.append(i)
            else:
                dire.append(i)

        member_ext = len(senate)
        
        while red and dire:
            curr_red_prior = red.popleft()
            curr_dire_prior = dire.popleft()

            if curr_red_prior > curr_dire_prior:
                dire.append(member_ext)
                member_ext += 1
            else:
                red.append(member_ext)
                member_ext += 1
        
        if not red:
            return "Dire"
        else:
            return "Radiant"

senate = "RD"
print(Solution.predictPartyVictory(senate))
