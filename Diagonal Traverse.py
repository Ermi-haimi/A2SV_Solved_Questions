class Solution:
    def findDiagonalOrder(self, mat):
        up = 1
        down = 2
        direction = up
        m = len(mat)
        n = len(mat[0])
        ans = []
        x = 0
        y = 0
        while(len(ans) < m*n):
            if(direction == up):
                while(x>-1 and y<n):
                    ans.append(mat[x][y])
                    x-=1
                    y+=1
                direction = down
                if(y==n):
                    y-=1
                    x+=2
                else:
                    x+=1
            else:
                while(y>-1 and x<m):
                    ans.append(mat[x][y])
                    x+=1
                    y-=1
                direction= up
                if(x==m):
                    x-=1
                    y+=2
                else:
                    y+=1
            

        return ans