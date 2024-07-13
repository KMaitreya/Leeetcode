class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = list(zip(positions, healths, directions, range(len(positions))))
        
        # Sort robots based on their positions
        robots.sort()
        
        stack = []
        for pos, health, direction, index in robots:
            if direction == 'R':
                # Robots moving to the right, push to stack
                stack.append((pos, health, direction, index))
            else:
                # Robots moving to the left, handle collisions
                while stack and stack[-1][2] == 'R':
                    prev_pos, prev_health, prev_direction, prev_index = stack.pop()
                    if prev_health > health:
                        prev_health -= 1
                        health = 0
                        stack.append((prev_pos, prev_health, prev_direction, prev_index))
                        break
                    elif prev_health < health:
                        health -= 1
                    else:
                        health = 0
                        break
                if health > 0:
                    stack.append((pos, health, direction, index))
        
        # Extract the remaining robots in their original order
        surviving_robots = sorted((pos, health, direction, index) for pos, health, direction, index in stack)
        result = [0] * len(positions)
        for pos, health, direction, index in surviving_robots:
            result[index] = health
        
        return [h for h in result if h > 0]
