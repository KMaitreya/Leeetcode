class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        obstacle_set = set(map(tuple, obstacles))

        # Directions: [North, East, South, West]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0  # Start at origin
        max_distance = 0
        direction_index = 0  # Start facing North

        for command in commands:
            if command == -1:  # Turn right
                direction_index = (direction_index + 1) % 4
            elif command == -2:  # Turn left
                direction_index = (direction_index - 1) % 4
            else:  # Move forward
                for _ in range(command):
                    new_x = x + directions[direction_index][0]
                    new_y = y + directions[direction_index][1]
                    if (new_x, new_y) not in obstacle_set:
                        x, y = new_x, new_y
                        max_distance = max(max_distance, x*x + y*y)
                    else:
                        break  # Stop if there is an obstacle

        return max_distance