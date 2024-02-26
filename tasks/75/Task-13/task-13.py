"""
1679. Max Number of K-Sum Pairs
Solved
Medium
Topics
Companies
Hint
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Initialize a hashmap to count occurrences of each number
        num_counts = {}
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1

        # Initialize count to keep track of the number of k-sum pairs
        count = 0

        for num in nums:
            complement = k - num
            # Check if the complement exists in the hashmap
            if complement in num_counts and num_counts[complement] > 0 and num_counts[num] > 0:
                # Special case handling when num is the same as its complement
                if num == complement and num_counts[num] < 2:
                    continue
                
                # Form a pair
                num_counts[num] -= 1
                num_counts[complement] -= 1
                count += 1

        return count

