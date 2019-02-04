import fileinput

numStrings = -1
set = 1
index = 0
pairIndex = 0

for line in fileinput.input():
    data = line.rstrip('\n')
    if numStrings == -1:
        numStrings = int(data)
        strings = [None] * numStrings
    else:
        if pairIndex == 0:
            strings[index] = str(data)
            pairIndex += 1
            index += 1
        else:
            strings[len(strings) - index] = str(data)
            pairIndex -= 1
        numStrings -= 1
        if numStrings == 0:
            print("SET " + str(set))
            for i in strings:
                print(i)
            index = 0
            pairIndex = 0
            set += 1
            numStrings = -1
