import fileinput

W = 0
N = 0
words = []

for line in fileinput.input():
    data = line.rstrip('\n').split(' ')
    print(data)
