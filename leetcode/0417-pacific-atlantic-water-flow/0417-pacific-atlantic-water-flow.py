class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights),len(heights[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(r,c,prev_h,visited):
            if((r,c) not in visited and r>=0 and c>=0 and r<rows and c<cols and heights[r][c]>=prev_h):
                visited.add((r,c))
                for rc,cc in directions:
                    dfs(r+rc,c+cc,heights[r][c],visited)
        
        a_visited = set()
        p_visited = set()
        for i in range(cols):
            dfs(0,i,heights[0][i],p_visited)
            dfs(rows-1,i,heights[rows-1][i],a_visited)
        for i in range(rows):
            dfs(i,0,heights[i][0],p_visited)
            dfs(i,cols-1,heights[i][cols-1],a_visited)
        ans = []
        for i in range(rows):
            for j in range(cols):
                if((i,j) in a_visited and (i,j) in p_visited):
                    ans.append([i,j])

        return ans
                
