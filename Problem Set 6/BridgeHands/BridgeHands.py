import fileinput
import collections

suits = {1:'C',2:'D',3:'S',4:'H'} #first priority of rank
ranks = {1:'2',2:'3',3:'4',4:'5',5:'6',6:'7',7:'8',8:'9',9:'T',10:'J',11:'Q',12:'K',13:'A'} #second priority of rank
compass = 'NESW'
dealerIndex = -1

N = []
NClubs = []
NDiamonds = []
NSpades = []
NHearts = []

E = []
EClubs = []
EDiamonds = []
ESpades = []
EHearts = []

S = []
SClubs = []
SDiamonds = []
SSpades = []
SHearts = []

W = []
WClubs = []
WDiamonds = []
WSpades = []
WHearts = []

start = False

for line in fileinput.input():
    data = line.rstrip('\n')
    if(len(data) == 1):
        if(not start):
            for i in range(len(compass)):
                if(data == compass[i]):
                    dealerIndex = i
        start = not start
    elif(start):
        for i in range(0, len(data), 2):
            if(dealerIndex == 4):
                dealerIndex = 0
            suit = data[i]
            rank = data[i+1]
            if(dealerIndex == 0):
                if(suit == 'C'):
                    EClubs.append(suit + rank)
                if(suit == 'D'):
                    EDiamonds.append(suit + rank)
                if(suit == 'S'):
                    ESpades.append(suit + rank)
                if(suit == 'H'):
                    EHearts.append(suit + rank)
            if(dealerIndex == 1):
                if(suit == 'C'):
                    SClubs.append(suit + rank)
                if(suit == 'D'):
                    SDiamonds.append(suit + rank)
                if(suit == 'S'):
                    SSpades.append(suit + rank)
                if(suit == 'H'):
                    SHearts.append(suit + rank)
            if(dealerIndex == 2):
                if(suit == 'C'):
                    WClubs.append(suit + rank)
                if(suit == 'D'):
                    WDiamonds.append(suit + rank)
                if(suit == 'S'):
                    WSpades.append(suit + rank)
                if(suit == 'H'):
                    WHearts.append(suit + rank)
            if(dealerIndex == 3):
                if(suit == 'C'):
                    NClubs.append(suit + rank)
                if(suit == 'D'):
                    NDiamonds.append(suit + rank)
                if(suit == 'S'):
                    NSpades.append(suit + rank)
                if(suit == 'H'):
                    NHearts.append(suit + rank)
            dealerIndex += 1

print(NClubs)
NClubs.sort(key=)
print(NClubs)
