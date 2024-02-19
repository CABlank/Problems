class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        tail = -1
        head = 0
        result = 0

        while head < len(s):
            if s[head] in letters:
                tail = max(tail, letters[s[head]])

            letters[s[head]] = head
            result = max(result, head - tail)
            head += 1

        return result

# Create an instance of the Solution class
sol = Solution()

# Call the method on the instance
print(sol.lengthOfLongestSubstring("abcabcbb"))
