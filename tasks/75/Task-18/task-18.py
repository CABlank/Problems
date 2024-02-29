class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        n = len(gain)  
        currentSum = 0	
        maxSum = 0

        for i in range(0, n):

            currentSum = gain[i] + currentSum

            maxSum = max(currentSum, maxSum)

        return maxSum