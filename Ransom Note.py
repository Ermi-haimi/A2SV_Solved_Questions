from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_freq = Counter(ransomNote)
        maga_freq = Counter(magazine)

        for key in ran_freq:
            if(key not in maga_freq):
                return False
            else:
                if(ran_freq[key]>maga_freq[key]):
                    return False

        return True