class Solution:
    def spiralOrder(self, matrix):

        m,n = len(matrix), len(matrix[0])
        i,j = 0,0
        ans = []

        up_w=0
        right_w=n
        down_w=m
        left_w=-1

        right,down,left,up = 1,2,3,4
        direction = right 

        while(len(ans)<m*n):
            if(direction == right):
                while(j<right_w):
                    ans.append(matrix[i][j])
                    j+=1
                right_w -=1
                i,j=i+1,j-1
                direction = down 
            elif(direction == down):
                while(i<down_w):
                    ans.append(matrix[i][j])
                    i+=1
                down_w -=1
                i,j=i-1,j-1
                direction = left
            elif(direction == left):
                while(j>left_w):
                    ans.append(matrix[i][j])
                    j-=1
                left_w +=1
                i,j=i-1,j+1
                direction = up
            else:
                while(i>up_w):
                    print(i,j)
                    ans.append(matrix[i][j])
                    i-=1
                up_w +=1
                i,j=i+1,j+1
                direction = right
        return ans

