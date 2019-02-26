import fileinput

# W = 0
# N = 0
# row = []
wordsLeft = -1
max = 0


for line in fileinput.input():
    data = line.rstrip('\n').split(' ')
    if wordsLeft == -1:
        max = data[0]
        wordsLeft = data[1]
    else:
        for word in data:
            


#     W = data[0]
#     if N:
#         N = data[1]
#     else:
#         N = 0
#     row = [0] * int(W)
#     wordsLeft = N
# else:
#     wordLengths = data
#     index = 0
#     for i in range(len(wordLengths) - 1):
#         for j in range(int(wordLengths(i))):
#             row[j-1 + index] = "a"
#         index = wordLengths[i] + 1
#     wordsLeft = -1
