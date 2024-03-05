class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}

        for num in arr:
            if num in occurrences:
                occurrences[num] += 1
            else:
                occurrences[num] = 1

        uniqueOccurrences = set()
        for count in occurrences.values():
            if count in uniqueOccurrences:
                return False
            uniqueOccurrences.add(count)

        return True