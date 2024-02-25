class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0

        i = 0
        j = len(height) - 1


        while i < j:

            minHeight = min(height[i], height[j])
            area = minHeight * (j - i) 
            maxArea = max(maxArea, area)

            # Move the pointer pointing to the shorter line inward
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxArea