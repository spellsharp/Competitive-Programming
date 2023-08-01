n = int(input())
coin_list = []
coin_list = list(map(int, input().split()))

totalValue = 0
for i in coin_list:
    totalValue += i

coin_list.sort(reverse=True)

    
