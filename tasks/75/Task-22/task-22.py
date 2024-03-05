class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if both strings have the same unique characters
        if set(word1) != set(word2):
            return False

        # Count character frequencies for both strings
        from collections import Counter
        frequency_count_word1 = Counter(word1)
        frequency_count_word2 = Counter(word2)

        # Sort and compare the frequency counts
        sorted_frequencies_word1 = sorted(frequency_count_word1.values())
        sorted_frequencies_word2 = sorted(frequency_count_word2.values())
        
        return sorted_frequencies_word1 == sorted_frequencies_word2
