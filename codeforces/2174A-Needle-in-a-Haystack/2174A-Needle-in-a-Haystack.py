from collections import Counter
n = int(input())
for _ in range(n):
    s = input()
    t = input()
    
    ns = len(s)
    

    possible =True

    t_counter = Counter(t)
    for i in range(ns):
        if(t_counter[s[i]] <= 0):
            possible = False
            break
        else:
            t_counter[s[i]]-=1
    
    t_list = (sorted(t_counter.keys()))
    nt = len(t_list)
    si = 0
    ti=0

    ans=[]

    
    if possible:
        while(ti<nt):
            if(t_counter[t_list[ti]] > 0):
                if(si<ns and s[si]<=t_list[ti]):
                    ans.append(s[si])
                    si+=1
                else:
                    temp = t_list[ti]*t_counter[t_list[ti]]
                    ti+=1
                    ans.append(temp)
            else:
                ti+=1
        
        if(si<ns):
            ans.append(s[si:])
        
        print("".join(ans))
    else:
        print("Impossible")