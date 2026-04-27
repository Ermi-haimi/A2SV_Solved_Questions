class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        rows = len(grid)
        cols = len(grid[0])
        def in_bound(r,c):
            if(r<rows and r>-1 and c<cols and c>-1):
                return True
            return False
        
        visited = set()
        def dfs(row,col):
            print(row,col)
            visited.add((row,col))
                
            for rc,cc in directions:
                if(in_bound(row+rc,col+cc) and (row+rc,col+cc) not in visited) and grid[row+rc][col+cc]=="1":
                    dfs(row+rc,col+cc)
        count=0
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j]=='1' and (i,j) not in visited):
                    print("aaaaaa")
                    dfs(i,j)
                    print("bbbbbbbb")
                    count+=1
        
        return count
