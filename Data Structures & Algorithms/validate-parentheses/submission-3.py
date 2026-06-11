class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            '(': ')', 
            '{': '}', 
            '[': ']'
        }

        stack = []
        for i in s:
            if i in char_map:
                stack.append(char_map[i])
                continue
            if len(stack) == 0 or stack.pop() != i:
                return False
        return len(stack) == 0