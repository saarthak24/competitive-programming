import fileinput

direction = 0
    #negative direction implies moving left
    #positive direction implies moving right
yellowSteps = 0
testCases = 0
startIndex = -1
tiles = []
tileLength = 0
totalSteps = 0

for line in fileinput.input():
    data = line.rstrip('\n').split(' ')
    if len(data) is 1:
        try:
            testCases = int(data[0])
        except:
            continue
    elif(len(data) is 2):
        tileLength = int(data[0])
        totalSteps = int(data[1])
    elif(len(data) > 2):
        tiles = data
        index = 0
        for i in tiles:
            if(int(i) is 2):
                startIndex = index
                direction = 1
            if(int(i) is 3):
                startIndex = index
                direction = -1
            index += 1
        while(totalSteps >= 0):
            if(startIndex is 0):
                direction *= -1
            elif(startIndex is (len(tiles) - 1)):
                direction *= -1
            if(direction < 0):
                if(int(tiles[startIndex]) == 0):
                    yellowSteps += 1
                startIndex -= 1
            else:
                if(int(tiles[startIndex]) == 0):
                    yellowSteps += 1
                startIndex += 1
            totalSteps -= 1
        print(yellowSteps)
        direction = 0
        yellowSteps = 0
        testCases = 0
        startIndex = -1
        tiles = []
        tileLength = 0
        totalSteps = 0
