inpStr = input()

capsNum = 0

for char in inpStr:
    if char.isupper():
        capsNum += 1
if capsNum == len(inpStr):
    print(inpStr.lower())
elif inpStr[0].islower() and inpStr[1:].isupper():
    print(inpStr[0].upper() + inpStr[1:].lower())
elif len(inpStr) == 1:
    print(inpStr.upper())
else:
    print(inpStr)
