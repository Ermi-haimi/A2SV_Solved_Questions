n = int(input())
contests = list(map(int, input().split()))
contests.sort()
day = 1

for num in contests:
    if num>=day:
        day+=1

print(day-1)