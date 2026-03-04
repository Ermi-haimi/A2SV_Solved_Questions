t = int(input())
for _ in range(t):
    n = int(input())
    red = list(map(int,input().split()))
    m = int(input())
    blue = list(map(int,input().split()))

    for i in range(1,n):
        red[i] = red[i]+red[i-1]
    for i in range(1,m):
        blue[i] = blue[i]+blue[i-1]
    
    red_mx = max(red)
    blue_mx = max(blue)
    both = red_mx+blue_mx
    mx = max(red_mx, blue_mx, both)

    print(max(0, mx))