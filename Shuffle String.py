class Solution:
    def restoreString(self, s, indices) -> str:
        n = len(s)
        arr = [0]*n
        for i in range(n):
            arr[indices[i]] = s[i]
        
        return "".join(arr)