class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        result = []

        maxLength = max(len(word1),len(word2) )

        for i in range (maxLength):

            if i < len(word1):
                result.append(word1[i])

            if i < len(word2):
                result.append(word2[i])

        return ''.join(result)