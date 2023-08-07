n, t = list(map(int, input().split()))

def func():
    for i in range(pow(10, n-1), pow(10,n)):
        if i % t == 0:
            print(i)
            return i
    print(-1)
    return -1

func()