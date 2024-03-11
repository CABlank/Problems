class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currentString = ""
        k = 0
        
        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)  # Consider multi-digit numbers
            elif char == '[':
                # Push the current state to the stack
                stack.append((currentString, k))
                currentString = ""  # Reset currentString
                k = 0  # Reset k
            elif char == ']':
                # Pop the last state and decode the current segment
                prevString, num = stack.pop()
                currentString = prevString + num * currentString
            else:
                # Append the current character to the currentString
                currentString += char
        
        return currentString
