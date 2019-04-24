import fileinput

firstLine = True
n = 3
nthLargestValues = []

for line in fileinput.input():
    data = list(map(int, line.rstrip('\n').split(' '))) #splits each line into list of integers
    if(firstLine is True):
        numSets = data[0]
        firstLine = False
    else:
        data.pop(0)
        dataSet = data
        dataSet.sort()
        nthLargestValues.append(dataSet[len(dataSet)-n])
        print(len(nthLargestValues),nthLargestValues[len(nthLargestValues)-1])
