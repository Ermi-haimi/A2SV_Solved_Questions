class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n= len(citations)
        left = 0
        right = n-1
        ans = 0
        while(left<=right):
            mid = left+(right-left)//2
            if(citations[mid] >= n-mid):
                ans =mid
                right = mid-1
            else:
                left=mid+1
        if(citations[ans]==0):
            return 0
        return n-ans


            
