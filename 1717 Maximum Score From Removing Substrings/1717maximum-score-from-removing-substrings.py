class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def remove_substring(s, sub1, sub2, points):
            stack = []
            count = 0
            for char in s:
                if stack and stack[-1] == sub1 and char == sub2:
                    stack.pop()
                    count += points
                else:
                    stack.append(char)
            return ''.join(stack), count
        
        if x > y:
            s, points = remove_substring(s, 'a', 'b', x)
            s, points2 = remove_substring(s, 'b', 'a', y)
        else:
            s, points = remove_substring(s, 'b', 'a', y)
            s, points2 = remove_substring(s, 'a', 'b', x)
        
        return points + points2