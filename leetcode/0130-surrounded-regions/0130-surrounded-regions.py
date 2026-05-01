class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cols = len(board[0])
        rows = len(board)
        visited = [[0] * cols for _ in range(rows)]

        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        def dfs(r,c):
            if(r>=0 and r<rows and c >= 0 and c<cols and board[r][c]=='O'):
                board[r][c]='T'
                for rc,cc in directions:
                    dfs(r+rc,c+cc)
        
        for i in range(cols):
            if(board[0][i]=='O'):
                dfs(0,i)
        for i in range(cols):
            if(board[rows-1][i]=='O'):
                dfs(rows-1,i)
        for i in range(rows):
            if(board[i][0]=='O'):
                dfs(i,0)
        for i in range(rows):
            if(board[i][cols-1]=='O'):
                dfs(i,cols-1)
        for i in range(rows):
            for j in range(cols):
                if(board[i][j]=='O'):
                    board[i][j]='X'
                elif(board[i][j]=='T'):
                    board[i][j]='O'


