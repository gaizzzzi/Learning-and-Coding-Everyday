class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # one pass
        stack = []
        for asteroid in asteroids:
            if not stack or not ((asteroid < 0) and (stack[-1] > 0)):
                stack.append(asteroid)
            else:
                while asteroid and (stack and (asteroid < 0) and (stack[-1] > 0)):
                    tmp = stack.pop()
                    if abs(tmp) > abs(asteroid):
                        asteroid = tmp
                    elif tmp + asteroid == 0:
                        asteroid = 0
                if asteroid:
                    stack.append(asteroid)
        return stack