import fileinput

dist = 0
pairs = 0
last_time = 0

for line in fileinput.input():
    data = line.rstrip('\n').split(' ')
    # for i in data:
    #     int(i)
    if len(data) == 1:
        pairs = int(data[0])
    else:
        dist += int(data[0]) * (int(data[1]) - last_time)
        pairs -= 1
        last_time = int(data[1])

    if pairs == 0:
        print(str(dist) + " miles")
        dist = 0
        last_time = 0
