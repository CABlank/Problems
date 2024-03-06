class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        length = len(grid)
        count = 0

        for i in range(length):
            column_array = []

            for j in range(length):
                column_array.append(grid[j][i])


            for j in range(length):
                if grid[j] == column_array:
                    count += 1

        return count