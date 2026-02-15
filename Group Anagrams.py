class Solution:
    def groupAnagrams(self, strs):
        store = {}
        for word in strs:
            wordl = list(word)
            wordl.sort()
            words = "".join(wordl)
            if(words in store):
                store[words].append(word)
            else:
                store[words] = [word]
        
        ans = []
        for val in store.values():
            ans.append(val)
        return ans