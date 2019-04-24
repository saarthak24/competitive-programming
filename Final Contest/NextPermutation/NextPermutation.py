import fileinput

firstLine = True

for line in fileinput.input():
    data = list(map(int, line.rstrip('\n').split(' '))) #splits each line into list of integers
    if(firstLine is True):
        numSets = data[0]
        firstLine = False
    else:
        pivotFound = False
        input = data[1]
        inputDigits = [int(digit) for digit in str(input)]
        inputLength = len(inputDigits)
        previousDigit = inputDigits[len(inputDigits) - 1]
        for i in range(len(inputDigits) - 2, -1, -1):
            previousDigit = inputDigits[i + 1]
            curDigit = inputDigits[i]
            if(curDigit < previousDigit):
                pivot = curDigit
                pivotIndex = i
                pivotFound = True
                rightOfPivot = []
                break
        smallestDigit = 10
        for i in range(pivotIndex + 1, len(inputDigits), 1):
            rightOfPivot.append(inputDigits[i-len(rightOfPivot)])
            if(rightOfPivot[len(rightOfPivot)-1] < smallestDigit and rightOfPivot[len(rightOfPivot)-1] > pivot):
                smallestDigit = rightOfPivot[len(rightOfPivot)-1]
                smallestDigitIndex = len(rightOfPivot)-1
            inputDigits.pop(pivotIndex + 1)
        if(pivotFound):
            temp = pivot
            inputDigits[pivotIndex] = smallestDigit
            rightOfPivot[smallestDigitIndex] = temp
            #inputDigits[smallestDigitIndex] = temp
            rightOfPivot.sort()
            finalDigits = inputDigits+rightOfPivot
            print(data[0], int(''.join(str(i) for i in finalDigits)))
        else:
            print(data[0], 'BIGGEST')
