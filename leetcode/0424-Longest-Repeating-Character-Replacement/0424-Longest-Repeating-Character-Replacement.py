class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = [0]*26
        left = 0
        right = 0
        mx = 0
        n =len(s)
        tot = 0
        mx_len = 0
        for right in range(n):
            ind = ord(s[right])
            curr = ind%ord("A")

            seen[curr] +=1
            mx = max(seen)
            tot = right -left+1
            while(tot-mx >k):
                ind = ord(s[left])
                curr = ind%ord("A")
                seen[curr] -=1
                tot-=1
                left+=1
                mx = max(seen)
            mx_len = max(mx_len,tot)


        return mx_len