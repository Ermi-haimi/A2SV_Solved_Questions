t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    stripe = input()
    left = 0
    
    w = 0
    min_w = 0
    for right in range(k):
        if(stripe[right] == "W"):
            w+=1
            min_w+=1
    
    for right in range(k,n):
        if stripe[left] == "W":
            w-=1
        if(stripe[right] == "W"):
            w+=1
        left+=1
        min_w = min(w,min_w)
    
    print(min_w)