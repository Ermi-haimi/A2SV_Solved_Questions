class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p=0
        ans = -1
        for i in range(len(haystack)):
            p=0
            if haystack[i] == needle[p]:
                l = i
                while(l<len(haystack) and p<len(needle) and haystack[l] == needle[p]):
                    p+=1
                    l+=1
            if(p==len(needle)):
                ans = l-p
                break
        
        return ans