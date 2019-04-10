import fileinput
import collections
import itertools

firstLine = True

for line in fileinput.input():
    data = line.rstrip('\n')
    if(data == '0 0'):
        break
    if(firstLine):
        data = data.split(' ')
        unknowns = [None] * int(data[0])
        index = 1
        while(index < len(data) - 1):
            unknowns[index-1] = int(data[index])
            index += 1
        permutations = list(itertools.permutations(unknowns))
        result = int(data[len(data) - 1])
    else:
        found = False
        expression = list(data)
        modified = list(data)
        for i in permutations:
            index = 0
            for char in range(len(expression)):
                if(str(expression[char]).isalpha()):
                    modified[char] = str(i[index])
                    index += 1
            if(int(eval("".join(modified))) is result):
                found = True
                break
            else:
                modified = list(data)
        if(found):
            print("YES")
        else:
            print("NO")
    firstLine = not firstLine
