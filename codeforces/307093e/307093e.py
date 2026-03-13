n,k = map(int, input().split())
nums = list(map(int, input().split()))
l = 0
freq = {}
ans =0
for r in range(n):
    if(nums[r] in freq):
        freq[nums[r]]+=1
    else:
        freq[nums[r]]=1
    
    if(len(freq) >k):
        while(len(freq) >k):
            freq[nums[l]]-=1
            if(freq[nums[l]] ==0):
                freq.pop(nums[l])
            l+=1
    ans+=r-l+1

print(ans)