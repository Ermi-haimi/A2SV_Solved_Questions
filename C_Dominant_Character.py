from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = 0
    
    window = 2
    found = False
    while(not found and window<=7):
        if(window>n):
            break
        left = 0
        a = b = c = 0
        right = window
        # print(right)
        for i in range(right):
            if s[i] =="a":
                # print(i)
                a+=1
            elif s[i] =="b":
                b+=1
            else:
                c+=1
        if(a>b and a>c):
            found=True
            ans = right-left
            break
        while(right<n):
            if(s[left]=="a"):
                a-=1
            elif(s[left] =="b"):
                b-=1
            else:
                c-=1
            if(s[right]=="a"):
                a+=1
            elif(s[right] =="b"):
                b+=1
            else:
                c+=1
            right+=1
            left+=1
            if(a>b and a>c):
                found=True
                ans = right-left
                break
        window+=1
    if(found):
        print(ans)
    else:
        print(-1)
