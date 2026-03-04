class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r = len(matrix)+1
        c = len(matrix[0])+1
        self.pre = [[0 for _ in range(c)] for _ in range(r)]
        print(matrix)
        print(self.pre)

        for i in range(1,r):
            for j in range(1,c):
                self.pre[i][j] = matrix[i-1][j-1]+self.pre[i-1][j]+self.pre[i][j-1]-self.pre[i-1][j-1]

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.pre[row2+1][col2+1]-self.pre[row2+1][col1]-self.pre[row1][col2+1]+self.pre[row1][col1]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)