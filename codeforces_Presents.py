n = int(input())
a = []
a = input().split()
a = list(map(int, a))
b = []

for i in range(n):
    index = a.index(i+1) + 1
    b.append(index)
for i in b:
    print(i, end=' ')
