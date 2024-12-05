class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Check if str1 and str2 can be concatenated to match each other
        if str1 + str2 != str2 + str1:
            return ""

        # Find the GCD of the lengths of the two strings
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        gcdLength = gcd(len(str1), len(str2))
        return str1[:gcdLength]