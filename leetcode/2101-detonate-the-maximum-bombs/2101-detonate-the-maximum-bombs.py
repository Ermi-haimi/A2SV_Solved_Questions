from collections import defaultdict
from math import sqrt
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        n =len(bombs)
        for i in range(n):
            x1,y1,r1 = bombs[i]
            for j in range(i+1,n):
                x2,y2,r2 = bombs[j]
                d = sqrt((x1-x2)**2 +(y1-y2)**2)
                if(d<=r1):
                    adj[i].append(j)
                if(d<=r2):
                    adj[j].append(i)
        
        def dfs(num,visited):
            if(num not in visited):
                visited.add(num)
                for i in adj[num]:
                    dfs(i,visited)
            
            return len(visited)
        
        ans =0
        for i in range(n):
            ans = max(ans, dfs(i,set()))
        return ans



                