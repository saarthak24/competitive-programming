import fileinput

for line in fileinput.input():
    data = line.rstrip('\n').split(' ')
