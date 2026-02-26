n,s = map(int, input().split())
nums = list(map(int, input().split()))
left = 0
right = 0
curr_sum = 0
count = 0
while(right<n):
    curr_sum+=nums[right]
    if(curr_sum>=s):
        while(left<=right and curr_sum>=s):
            count+=1
            count+=n-right-1
            curr_sum-=nums[left]
            left+=1
    right+=1

print(count)


