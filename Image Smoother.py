class Solution:
    def imageSmoother(self, img):
        m = len(img)
        n = len(img[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        # xi =0
        # yi =0
        # xf = 3
        # yf = 3
        # if(m<3):
        #     xf=m
        # if(n<3):
        #     yf = n
        # while(xf<=m and yf<=n):
        for i in range(m):
            for j in range(n):
                count=1
                tot=img[i][j]
                if(i-1>=0):
                    count+=1
                    tot+=img[i-1][j]
                    if(j-1>=0):
                        tot+=img[i-1][j-1]
                        count+=1
                    if(j+1<n):
                        tot+=img[i-1][j+1]
                        count+=1
                if(i+1<m):
                    tot+=img[i+1][j]
                    count+=1
                    if(j-1>=0):
                        tot+=img[i+1][j-1]
                        count+=1
                    if(j+1<n):
                        tot+=img[i+1][j+1]
                        count+=1
                if(j+1<n):
                    tot+=img[i][j+1]
                    count+=1
                if(j-1>=0):
                    tot+=img[i][j-1]
                    count+=1
                ans[i][j] = tot//count
            
        return ans

