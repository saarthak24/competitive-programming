import fileinput

trip = 0

for line in fileinput.input():
    data = []
    data = line.rstrip('\n').split(' ')
    if data[1]==str(0):
        break
    diameter = float(data[0])
    circumference = diameter * 3.1415927
    distance_inch = circumference * int(data[1])
    distance_mile = (distance_inch/12)/5280
    mph = round(distance_mile / (float(data[2])/3600), 2)
    print('Trip #' + str(trip) + ': ' + str(round(distance_mile,2)) + ' ' + str(mph))
    trip += 1
