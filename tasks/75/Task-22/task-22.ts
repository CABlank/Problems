function closeStrings(word1: string, word2: string): boolean {
    // Check if both strings have the same unique characters
    const uniqueCharsWord1 = new Set(word1);
    const uniqueCharsWord2 = new Set(word2);

    if (uniqueCharsWord1.size !== uniqueCharsWord2.size) return false;

    for (let char of uniqueCharsWord1) {
        if (!uniqueCharsWord2.has(char)) return false;
    }

    // Count character frequencies for both strings
    const frequencyCountWord1 = getFrequencyCount(word1);
    const frequencyCountWord2 = getFrequencyCount(word2);

    // Sort and compare the frequency counts
    const sortedFrequenciesWord1 = Object.values(frequencyCountWord1).sort((a, b) => a - b);
    const sortedFrequenciesWord2 = Object.values(frequencyCountWord2).sort((a, b) => a - b);

    return sortedFrequenciesWord1.length === sortedFrequenciesWord2.length &&
           sortedFrequenciesWord1.every((value, index) => value === sortedFrequenciesWord2[index]);
}

function getFrequencyCount(word: string): Record<string, number> {
    const count: Record<string, number> = {};
    for (let char of word) {
        count[char] = (count[char] || 0) + 1;
    }
    return count;
}