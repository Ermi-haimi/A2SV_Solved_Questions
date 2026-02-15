from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        if(len(word1) != len(word2)):
            return False

        for key in freq1:
            if key not in freq2:
                return False

        freq11 = Counter(freq1.values())
        freq12 = Counter(freq2.values())


        for key,val in freq11.items():
            if(key not in freq12):
                return False
            else:
                if(freq12[key] != val):
                    return False
        
        return True