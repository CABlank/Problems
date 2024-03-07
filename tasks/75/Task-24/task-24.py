class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char != '*':
                stack.append(char)
            elif stack:  # Check if the stack is not empty before popping
                stack.pop()
        return ''.join(stack)