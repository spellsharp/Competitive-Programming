compareStr = "hello"
string = input()

count = 0
for char in string:
    if char == compareStr[count]:
        count += 1
    if count == 5:
        break
    

if count == 5:
    print("YES")
else: 
    print("NO")