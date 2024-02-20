class Solution:
    def reverseVowels(self, s: str) -> str:  # Add 'self' here
        vowels = 'aeiouAEIOU'
        stringList = list(s)  # Convert the string to a list
        i, j = 0, len(s) - 1

        while i < j:
            if stringList[i] in vowels and stringList[j] in vowels:
                stringList[i], stringList[j] = stringList[j], stringList[i]
                i += 1
                j -= 1
            if stringList[i] not in vowels:
                i += 1
            if stringList[j] not in vowels:
                j -= 1

        return ''.join(stringList)

sol = Solution()
print(sol.reverseVowels("leetcode"))
