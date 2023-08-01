n = int(input())
totalCount = 0
for i in range(n):
    p, v, t = map(int, input().split())
    count = 0
    if p == 1:
        count += 1
    if v == 1:
        count += 1
    if t == 1:
        count += 1
    
    if count >= 2:
        totalCount += 1
print(totalCount)


