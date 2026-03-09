class Solution:
    def removeStars(self, s: str) -> str:
        store = []
        for c in s:
            if c == "*" and len(store) >0:
                store.pop()
            else:
                store.append(c)
        
        return "".join(store)
        