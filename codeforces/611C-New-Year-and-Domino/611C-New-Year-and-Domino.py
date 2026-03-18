r,c=map(int, input().split())
mat = []
for _ in range(r):
    row = list(input())
    mat.append(row)

horizontal = [[0]*c for _ in range(r)]
vertical = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if(j<c-1 and mat[i][j] =='.' and mat[i][j+1] =='.'):
            horizontal[i][j]=1
        if(i<r-1 and mat[i][j] =='.' and mat[i+1][j] =='.'):
            vertical[i][j]=1

pre_h = [[0]*(c+1) for _ in range(r+1)]
pre_v = [[0]*(c+1) for _ in range(r+1)]

for i in range(1,r+1):
    for j in range(1,c+1):
        pre_h[i][j] = horizontal[i-1][j-1]+pre_h[i-1][j]+pre_h[i][j-1]-pre_h[i-1][j-1]
        pre_v[i][j] = vertical[i-1][j-1]+pre_v[i-1][j]+pre_v[i][j-1]-pre_v[i-1][j-1]


q = int(input())
for _ in range(q):
    r1,c1,r2,c2 =map(int, input().split())
    
    c2-=1
    
    h = pre_h[r2][c2]-pre_h[r2][c1-1]-pre_h[r1-1][c2]+pre_h[r1-1][c1-1]  
    r2-=1
    c2+=1
    v = pre_v[r2][c2]-pre_v[r2][c1-1]-pre_v[r1-1][c2]+pre_v[r1-1][c1-1]
    print(h+v)