class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for dir_size in asteroids:
            if not stack: 
                stack.append(dir_size)
                continue

            while dir_size < 0 and stack[-1]: # while there is collision
                if 0 - stack[-1] == dir_size:
                    stack.pop()
                    break
                elif 0 - stack[-1] > dir_size: # the current dir_size is bigger than size of last asteriod
                    stack.pop()
                else: # the current dir_size is smaller than size of last asteriod
                    break # next dir_size
            else:
                stack.append(dir_size)
        
        return stack








        
asteroids = [-2,-1,1,2]

print(asteroidCollision(asteroids))