import fileinput

correctList = []
scanned = ""
NumFound = False
codeIndex = -1
numcodes = 0
code = ""
codes = []

for line in fileinput.input():
    data = line.rstrip('\n')
    if NumFound:
        if codeIndex > 0:
            codes[numcodes - codeIndex] = str(data)
            codeIndex -= 1
    if not NumFound:
        try:
            if int(data) and (1 <= int(data) <= 1000) :
                numcodes = int(data)
                codeIndex = numcodes
                codes = [None] * numcodes
                NumFound = True
            else:
                code = list(data)
        except:
            code = list(data)

for i in codes:
    charArray = list(i)
    isCorrect = True
    for char in range(len(charArray) - 1):
        if charArray[char] == code[char] or code[char] == "*":
            continue
        else:
            isCorrect = False
    if isCorrect:
        correctList.append(i)

print(len(correctList))
for i in correctList:
    print(i)
