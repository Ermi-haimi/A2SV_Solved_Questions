n,k,q = map(int,input().split())
recipes = [0]*200002
for _ in range(n):
    mn,mx=map(int,input().split())
    recipes[mn]+=1
    recipes[mx+1]-=1

for i in range(1,200002):
    recipes[i]=recipes[i]+recipes[i-1]


valid = [0]*200002

for ind,val in enumerate(recipes):
    if(val>=k):
        valid[ind]=1

for i in range(1,200002):
    valid[i]=valid[i]+valid[i-1]


for _ in range(q):
    l,r = map(int,input().split())
    print(valid[r]-valid[l-1])