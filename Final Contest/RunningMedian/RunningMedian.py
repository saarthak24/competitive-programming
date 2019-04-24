import fileinput
import statistics

firstLine = True
setProcessed = True

for line in fileinput.input():
    data = list(map(int, line.rstrip('\n').split(' '))) #splits each line into list of integers
    if(firstLine is True):
        numSets = data[0]
        firstLine = False
    else:
        if(setProcessed is False):
            setLeft = min(setLength - len(curSet), len(data))
            index = 1
            while(setLeft > 0 and index > 0 and (index%10) is not 0):
                if((index % 2) is 1):
                    curSet.append(data[index-1])
                    curMedians.append(statistics.median(curSet))
                else:
                    curSet.append(data[index-1])
                setLeft -= 1
                index += 1
                if(setLeft is 0):
                    print(curMedians)
                    setProcessed = True
                    break
            continue
        if(setProcessed is True):
            curSet = []
            curMedians = []
            setIndex = data[0]
            setLength = data[1]
            setProcessed = False
