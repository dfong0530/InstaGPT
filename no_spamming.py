import csv

def getBlacklist():
    with open('blacklist.csv', 'r') as file:
        line = file.readline().strip()
        blacklist = set(line.split(','))

    return blacklist


def updateBlackList(blacklist):

    names = ','.join(blacklist)

    with open('blacklist.csv', 'w') as file:
        file.write(names)