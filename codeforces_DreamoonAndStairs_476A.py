#wrong


import sys
n, m = list(map(int, input().split()))

# n = 29
# m = 7
if n < m:
    print(-1)
    sys.exit()

if (n / 2) % m == 0:
    print(int(n/2))
elif (n // 2) % m == 0:
    print(n//2 + m)
elif (n - 1) / 2 % m == 0:
    print(int((n - 1) / 2))
elif (n - 1) // 2 % m == 0:
    print((n - 1) // 2 + m)    
else:
    print(-1)