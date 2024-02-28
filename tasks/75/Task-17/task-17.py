class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxLen = 0
        left = 0
        zeroCount = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                zeroCount += 1

            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            maxLen = max(maxLen, i - left)

        return maxLen