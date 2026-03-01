from collections import Counter
n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ac = Counter(a)
bc = Counter(b)
ans = 0


for num in ac:
    ans += ac[num]*bc[num]

print(ans)
