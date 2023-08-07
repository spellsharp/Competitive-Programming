n = int(input())
lst_of_Si = list(map(int, input().split()))
lst_of_Si.sort()
length = len(lst_of_Si)
taxis = 0

taxis += lst_of_Si.count(4)

count_3 = lst_of_Si.count(3)
count_1 = lst_of_Si.count(1)
if count_3 >= count_1:
    taxis += count_3
    count_1 = 0
else:
    taxis += count_3
    count_1 -= count_3

count_2 = lst_of_Si.count(2)
if count_2 % 2 == 0:
    taxis += count_2 // 2
else:
    taxis += count_2 // 2 + 1
    count_1 -= 2

if count_1 > 0:
    taxis += (count_1 + 3) // 4

print(taxis)