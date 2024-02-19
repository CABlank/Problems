class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        # Calculate the length of the longer word to ensure all characters are included
        maxLength = max(len(word1), len(word2))

        for i in range(maxLength):
            # Check if the current index is within the bounds of word1
            if i < len(word1):
                result.append(word1[i])
            # Check if the current index is within the bounds of word2
            if i < len(word2):
                result.append(word2[i])

        # Join the list of characters into a single string
        return ''.join(result)

sol = Solution()
print('Solution', sol.mergeAlternately('abc','pqr'))
