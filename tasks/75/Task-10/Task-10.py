"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0 
        for i in range(0, len(nums)):
            if nums[i] != 0:
                # Move the non-zero element to the position indicated by 'count'
                nums[count] = nums[i]
                if i != count:
                    # Set the original position to 0 since we've moved the non-zero element
                    nums[i] = 0
                count += 1

