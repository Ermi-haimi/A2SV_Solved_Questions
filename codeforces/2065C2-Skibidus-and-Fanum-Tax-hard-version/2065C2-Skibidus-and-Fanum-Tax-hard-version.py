def validj(preva,num,len_b,bl):
    left = 0
    right = len_b-1
    while(left <= right):
        mid = left +(right-left)//2
        if(bl[mid] >= preva+num):
            right=mid-1
        else:
            left=mid+1
    
    return left


t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    prev = float('-inf')
    flag = True



    for i in range(n):
        ind = validj(prev,a[i],m,b)

        if(ind < m):
            if(a[i]>=prev and a[i] < b[ind]-a[i]):
                prev = a[i]
            else:
                prev = b[ind]-a[i]
        else:
            if(a[i]>=prev):
                prev = a[i]
            else:
                flag = False
                break
    
    print("YES" if flag else "NO")