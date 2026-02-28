n,k = map(int, input().split())
nums = list(map(int, input().split()))
tot = nums[-1] - nums[0]
store = []
if(k ==1 ):
    print(tot)
else:
    for i in range(1,n):
        store.append(nums[i] - nums[i-1])

    store =sorted(store, reverse=True)


    print(tot-sum(store[:k-1]))