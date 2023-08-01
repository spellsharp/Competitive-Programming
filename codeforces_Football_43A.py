numDescriptions = int(input())
descriptionList = []
for description in range(numDescriptions):
    descriptionList.append(input())
teamList = []
for description in descriptionList:
    if description not in teamList:
        teamList.append(description)
    else:
        continue
count1 = 0
count2 = 0
for description in descriptionList:
    if description == teamList[0]:
        count1 += 1
    elif description == teamList[1]:
        count2 += 1

if count1 > count2:
    print(teamList[0])
else:
    print(teamList[1])

    