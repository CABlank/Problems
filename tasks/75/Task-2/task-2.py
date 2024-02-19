class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Function to find the GCD of two numbers
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Check if str1 and str2 have a common base
        if str1 + str2 != str2 + str1:
            return ""

        # Find the gcd of the lengths of str1 and str2
        length_gcd = gcd(len(str1), len(str2))

        # The GCD string is a substring of either str1 or str2 of length length_gcd
        gcd_str = str1[:length_gcd]

        # Return the GCD string
        return gcd_str

sol = Solution()
print('Solution:', sol.gcdOfStrings("ABABABAB", "ABAB"))  # Expected: "ABAB"
