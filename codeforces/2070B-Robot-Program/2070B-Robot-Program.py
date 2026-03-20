t = int(input())
for _ in range(t):
    n,x,k = map(int, input().split())
    com = input()
    pref = []
    curr = 0
    hit=False
    for c in com:
        if(c=='L'):
            curr-=1
        else:
            curr+=1

        pref.append(curr)
    
    for i in range(n):
        k-=1
        if(pref[i]==-x):
            hit=True
            break

    if(hit):
        step = 0
        hit=False
        for i in range(n):
            step+=1
            if(pref[i]==0):
                hit=True
                break
        
        if(hit):
            print((k//step)+1)
        else:
            print(1)
    else:
        print(0)