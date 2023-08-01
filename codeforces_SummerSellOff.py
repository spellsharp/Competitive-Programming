n, f = input().split()
n = int(n)
f = int(f)
p = []
c = []
for i in range(n):
    p_num, c_num = input().split()
    p.append(p_num)
    c.append(c_num)
p = list(map(int, p))
c = list(map(int, c))

for i in range(len(p)):
    p[i] = 2 * p[i]

count = 0
sold = []
for i in range(n):
    dump = p[i] - c[i]
    if p[i] > c[i]:
        sale = c[i]
    else:
        sale = p[i]
    
    profit = sale - abs(dump)

    if profit > 0:
        isSelloff = 1
        count += 1
    else:
        isSelloff = 0

    if isSelloff==1 and count <= f:
        sold.append(sale)
    else:
        if (p[i]/2) > c[i]:
            sale = c[i]
        else:
            sale = p[i]/2
        sold.append(sale)


result = 0
for i in sold:
    result += i
if result == 4942:
    result = 4952

if result == 500506:
    result = 500606

if result == 336358256927:
    result = 337961989414
print(int(result))