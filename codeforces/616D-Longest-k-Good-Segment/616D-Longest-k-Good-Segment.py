n,k = map(int,input().split())
nums = list(map(int,input().split()))

left = 0
long = 0

count = {}
ans_l = 0
ans_r = 0

for right in range(n):
    if(nums[right] in count):
        count[nums[right]]+=1
    else:
        count[nums[right]]=1
    if(len(count) >k):
        while(len(count)>k):
            if(count[nums[left]] >1):
                count[nums[left]]-=1
            else:
                del count[nums[left]]
            left+=1
    
    if(right-left+1 > long):
        long = right-left+1
        ans_l = left
        ans_r = right

print(ans_l+1, ans_r+1)