t = int(input())
for _ in range(t):
    n =int(input())
    nums = list(map(int, input().split()))
    ans=0
    
    for k in range (2,n):
        j = k-1
        i=0
        mx = max(nums[k],nums[n-1]-nums[k])
        while(i<j):
            if(nums[i]+nums[j] >mx ):
                ans+=j-i
                j-=1
            else:
                i+=1
    
    print(ans)