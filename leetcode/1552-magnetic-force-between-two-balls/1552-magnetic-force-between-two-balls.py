class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def possible(min_pos):
            prev = position[0]
            placed = 1
            for i in range(1,len(position)):
                if(position[i]-prev >= min_pos):
                    placed+=1
                    prev = position[i]
                    if placed == m:
                        return True
            return False
        
        position.sort()
        ans = -1
        left = 1
        right = position[-1]-position[0]
        while(left<=right):
            mid = left+(right-left)//2
            if(possible(mid)):
                ans = mid
                left=mid+1
            else:
                right=mid-1
        
        return ans if ans != -1 else position[-1]-position[0]