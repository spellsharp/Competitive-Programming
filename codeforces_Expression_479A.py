a = int(input())
b = int(input())
c = int(input())

caseList = []

case1 = a + b * c
case2 = a * b + c
case3 = a * (b + c)
case4 = (a + b) * c
case5 = a * b * c
case6 = a + b + c

caseList = [case1, case2, case3, case4, case5, case6]

caseList.sort()

print(caseList[-1])