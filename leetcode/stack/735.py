def asteroidCollision(asteroids):
    stack = []

    for dir_size in asteroids:
        while (stack and stack[-1] > 0 and dir_size < 0): # collision
            if stack[-1] < 0 - dir_size:
                stack.pop(-1)
            elif stack[-1] == 0 - dir_size:
                stack.pop(-1)
                break
            else:
                break
        else:
            stack.append(dir_size)
    
    return stack








        
asteroids = [-2,-1,1,2]

print(asteroidCollision(asteroids))