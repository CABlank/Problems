<?php
function mergeAlternately(string $word1, string $word2): string {
    $result = [];
    $maxLength = max(strlen($word1), strlen($word2));

    for ($i = 0; $i < $maxLength; $i++) {
        if ($i < strlen($word1)) {
            $result[] = $word1[$i];
        }
        if ($i < strlen($word2)) {
            $result[] = $word2[$i];
        }
    }

    return implode('', $result);
}

?>
