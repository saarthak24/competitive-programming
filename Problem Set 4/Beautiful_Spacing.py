
import fileinput

# W = 0
# N = 0
# row = []
wordsLeft = -1
max = 0
lines = 0

def space(list):
    global lines
    lines += 1
    leftoverLocal = []
    for word in list:
        global total
        total += int(word) + 1
        if total - 1 > max:
            leftoverLocal.append(word)
    global leftover
    leftover = leftoverLocal
    leftoverLocal = []
    total = 0
    # print(leftover)

for line in fileinput.input():
    data = line.rstrip('\n').split(' ')
    if wordsLeft == -1:
        max = int(data[0])
        wordsLeft = data[1]
    else:
        total = 0
        space(data)
        while leftover != []:
            space(leftover)
        print(lines)
        lines = 0
