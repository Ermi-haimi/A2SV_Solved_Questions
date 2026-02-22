class Solution:
    def findMinArrowShots(self, points) -> int:
        points  =sorted(points, key=lambda x:x[1])
        n = len(points)
        count = 0
        i = 0
        end = float("-inf")
        while(i<n):
            curr = points[i]
            if(curr[0]>end):
                count+=1
                end=curr[1]
            i+=1
        return count