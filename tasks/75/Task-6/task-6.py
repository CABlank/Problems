class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        start_index = 0
        end_index = len(words) - 1

        while start_index < end_index:
            # Swap the elements
            words[start_index], words[end_index] = words[end_index], words[start_index]
            
            # Move towards the middle
            start_index += 1
            end_index -= 1
        
        return ' '.join(words)

sol = Solution()

print(sol.reverseWords("hello world")) 
