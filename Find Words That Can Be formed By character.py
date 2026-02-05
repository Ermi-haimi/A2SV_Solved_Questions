from collections import Counter
class Solution:
    def countCharacters(self, words, chars: str) -> int:
        ans = 0
        chars = Counter(chars)
        for word in words:
            if Counter(word) <= chars:
                ans+=len(word)
        return ans