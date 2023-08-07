#incomplete

numCases = int(input())
for case in range(numCases):
    numMountains = int(input())
    heightsList = list(map(int, input().split()))
    heightsList.sort()
    #separate the sorted array at the middle
    lesserHeightsList = heightsList[:len(heightsList)//2]
    greaterHeightsList = heightsList[len(heightsList)//2:]
    
    #find a pair in lesserHeightsList whose absolute difference is least compared to other pairs
    pairList = []
    diffList = []
    minPair = []

    minimum = max(heightsList)
    for i in range(len(heightsList)):
        for j in range(len(heightsList)):
            if i != j:
                difference = abs(heightsList[i]-heightsList[j])
                if difference < minimum:
                    minimum = difference
                    pairList.append([heightsList[i], heightsList[j]])    
                    diffList.append(difference)

    minPair = pairList[diffList.index(min(diffList))]
    print(minPair)





