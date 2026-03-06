class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        row = [False]*m
        col = [False]*n
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == 0):
                    row[i] = True
                    col[j] = True
        
        for i in range(m):
            if row[i]:
                for c in range(n):
                    matrix[i][c] = 0
        for i in range(n):
            if col[i]:
                for c in range(m):
                    matrix[c][i] = 0
            

