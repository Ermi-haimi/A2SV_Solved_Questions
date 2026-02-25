t = int(input())
for _ in range(t):
    s = input()
    n =len(s)
    ans = []
    slow = 0
    fast = 0
    while(fast<n):
        count = 0
        while(fast<n and s[slow] == s[fast]):
            count+=1
            fast+=1
        if(count%2 !=0):
            ans.append(s[slow])
        slow = fast

    ans = set(ans)
    print("".join(sorted(ans)))