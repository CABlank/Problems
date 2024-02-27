class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        currentSum = 0
        maxSum = 0

        for j in range(0, k):
            if s[j] in vowels:
                currentSum += 1

        maxSum = currentSum

        for j in range(k, len(s)):
            if s[j] in vowels:
                currentSum += 1
            if s[j - k] in vowels:
                currentSum -= 1
            maxSum = max(maxSum, currentSum)

        return maxSum