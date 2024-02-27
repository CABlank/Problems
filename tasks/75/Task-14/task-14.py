class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = 0
        currentSum = 0
        i = 0
        j = 0

        while j < k:
            currentSum += nums[j]
            j += 1

        maxSum = currentSum

        while j < len(nums):
            currentSum = currentSum + nums[j] - nums[i]
            maxSum = max(maxSum, currentSum)
            i += 1
            j += 1

        return maxSum / k 