numCases = int(input())
x = 0
y = 0
z = 0
for case in range(numCases):
    inpX, inpY, inpZ = list(map(int, input().split()))
    x = x + inpX
    y = y + inpY
    z = z + inpZ

if x==0 and y==0 and z==0:
    print("YES")
else: print("NO")