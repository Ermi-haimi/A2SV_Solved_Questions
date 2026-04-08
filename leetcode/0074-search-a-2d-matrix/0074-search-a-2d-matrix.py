class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)

        low = 0
        high = n*m-1

        while(low<=high):
            mid = low + (high-low)//2
            r = mid//m
            c = mid%m
            if(matrix[r][c]==target):
                return True
            elif(matrix[r][c]>target):
                high = mid-1
            else:
                low=mid+1
        return False
            