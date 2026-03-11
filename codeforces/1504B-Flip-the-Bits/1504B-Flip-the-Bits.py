t = int(input())
for _ in range(t):
    n=int(input())
    a = input()
    b = input()

    zeros = 0
    ones = 0
    possible = True
    balanced = [False]*n
    for i in range(n):
        if(a[i]=="0"):
            zeros+=1
        else:
            ones+=1
        
        if(ones == zeros):
            balanced[i] = True


    flipped = 0
    for i in range(n-1,-1,-1):
        curr = a[i]
        if(flipped % 2 != 0):
            curr = "1" if a[i] == "0" else "0"
            
        if(curr == b[i]):
            continue

        if(not balanced[i]):
            possible = False
            break
            
        flipped+=1
        
    if possible:
        print("YES")
    else:
        print("NO")