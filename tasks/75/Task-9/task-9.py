"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:

        write_position = 0  
        count = 1 

        for i in range(len(chars)):
            if i + 1 < len(chars) and chars[i] == chars[i + 1]:
                count += 1
            else:
                # If the current character is not the same as the next one, or we're at the last character
                chars[write_position] = chars[i]  # Write the current character to its new position
                write_position += 1  # Move write position
                if count > 1:
                    # Convert count to a list of characters and append each to chars
                    for c in str(count):
                        chars[write_position] = c
                        write_position += 1
                count = 1 

        return write_position

# Example usage
sol = Solution()
chars = ["a", "a", "b", "b", "c", "c", "c"]
print(f"Compressed length: {sol.compress(chars)}")
print(f"Compressed array: {chars[:sol.compress(chars)]}")


        