from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed) 
        i = 0  

        while i < length and n > 0:
            # Check if the current spot is 0 and both neighbors (if exist) are also 0 or it's an edge case
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1  # Plant a flower here
                n -= 1 
                i += 2  
            else:
                i += 1 

            if n == 0: 
                break

        return n == 0  

# Create an instance of the Solution class
sol = Solution()

# Example usage
flowerbed = [1, 0, 0, 0, 1]
n = 1
print(sol.canPlaceFlowers(flowerbed, n))
