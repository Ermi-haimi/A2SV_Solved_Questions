class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        store = []
        n1 = len(word1)
        n2 = len(word2)
        i=0
        j=0
        while(i<n1 and j<n2):
            store.append(word1[i])
            store.append(word2[j])
            i+=1
            j+=1
        while(i<n1):
            store.append(word1[i])
            i+=1
        while(j<n2):
            store.append(word2[j])
            j+=1
        return "".join(store)
