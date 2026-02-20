class Solution:
    def pancakeSort(self, arr):
        n= len(arr)
        ans = []
        for i in range(n,0,-1):
            for ind,num in enumerate(arr):
                if(num == i):
                    if(num != ind+1):
                        ans.append(ind+1)
                        ans.append(num)
                        left = 0
                        right = ind
                        while(left<right):
                            arr[left],arr[right]=arr[right],arr[left]
                            left+=1
                            right-=1
                        left = 0 
                        right = num-1
                        while(left<right):
                            arr[left],arr[right]=arr[right],arr[left]
                            left+=1
                            right-=1
    
        return ans
