import math
import copy
mapMatrix = []

fileInput = open("input.txt", 'r')
for line in fileInput:

    lineList = []
    for char in line:
        if len(char.replace("\n", "")) != 0:
            lineList.append(char.replace("\n", ""))
    mapMatrix.append(lineList)


def HeuristicCalculation(pos1, pos2):
    return (abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1]))


def ExpandNode(mapMatrix, position, endPosition, isGround):
    expandedDict = {}
    if isGround:
        if mapMatrix[position[1]][position[0]+1] == "*":
            expandedDict[tuple([position[0]+1, position[1]])
                         ] = HeuristicCalculation([position[0]+1, position[1]], endPosition)
        if mapMatrix[position[1]][position[0]-1] == "*":
            expandedDict[tuple([position[0]-1, position[1]])
                         ] = HeuristicCalculation([position[0]-1, position[1]], endPosition)
        if mapMatrix[position[1]+1][position[0]] == "*":
            expandedDict[tuple([position[0], position[1]+1])
                         ] = HeuristicCalculation([position[0], position[1]+1], endPosition)
        if mapMatrix[position[1]-1][position[0]] == "*":
            expandedDict[tuple([position[0], position[1]-1])
                         ] = HeuristicCalculation([position[0], position[1]-1], endPosition)

        return expandedDict
    else:
        if mapMatrix[position[1]][position[0]+1] == "*" or mapMatrix[position[1]][position[0]+1] == "#":
            expandedDict[tuple([position[0]+1, position[1]])
                         ] = HeuristicCalculation([position[0]+1, position[1]], endPosition)
        if mapMatrix[position[1]][position[0]-1] == "*" or mapMatrix[position[1]][position[0]-1] == "#":
            expandedDict[tuple([position[0]-1, position[1]])
                         ] = HeuristicCalculation([position[0]-1, position[1]], endPosition)
        if mapMatrix[position[1]+1][position[0]] == "*" or mapMatrix[position[1]+1][position[0]] == "#":
            expandedDict[tuple([position[0], position[1]+1])
                         ] = HeuristicCalculation([position[0], position[1]+1], endPosition)
        if mapMatrix[position[1]-1][position[0]] == "*" or mapMatrix[position[1]-1][position[0]] == "#":
            expandedDict[tuple([position[0], position[1]-1])
                         ] = HeuristicCalculation([position[0], position[1]-1], endPosition)
        return expandedDict


def TrackProgress(mapMatrix, simpulHidup, position):
    if next(iter(simpulHidup))[0] == position[0]+1 and position[1] == next(iter(simpulHidup))[1]:
        mapMatrix[position[1]][position[0]] = "-"
    elif next(iter(simpulHidup))[0] == position[0]-1 and position[1] == next(iter(simpulHidup))[1]:
        mapMatrix[position[1]][position[0]] = "-"
    elif next(iter(simpulHidup))[0] == position[0] and position[1]+1 == next(iter(simpulHidup))[1]:
        mapMatrix[position[1]][position[0]] = "|"
    elif next(iter(simpulHidup))[0] == position[0] and position[1]-1 == next(iter(simpulHidup))[1]:
        mapMatrix[position[1]][position[0]] = "|"


def PrintHasilPencarianRute(mapMatrix, initialPosition, endPosition):
    mapMatrix[initialPosition[1]][initialPosition[0]] = "S"
    mapMatrix[endPosition[1]][endPosition[0]] = "G"
    for i in range(len(mapMatrix)):
        for j in range(len(mapMatrix[0])):
            print(mapMatrix[i][j], end="")
        print()


def GreedyBestFirstSearch(mapMatrix, initialPosition, endPosition, isGround):
    pathToDestination = []
    simpulHidup = ExpandNode(mapMatrix, initialPosition, endPosition, isGround)
    position = initialPosition
    while (position[0] != endPosition[0] or position[1] != endPosition[1]) and len(simpulHidup) != 0:
        simpulHidup = sorted(simpulHidup, key=simpulHidup.get)
        TrackProgress(mapMatrix, simpulHidup, position)
        position = next(iter(simpulHidup))
        simpulHidup = ExpandNode(mapMatrix, position, endPosition, isGround)
    PrintHasilPencarianRute(mapMatrix, initialPosition, endPosition)


mapMatrixGround = copy.deepcopy(mapMatrix)
mapMatrixAir = copy.deepcopy(mapMatrix)
print("Untuk Pasukan Pada Jalur Darat :")
GreedyBestFirstSearch(mapMatrixAir, [8, 4], [45, 25], False)
print()
print("Untuk Pasukan Pada Jalur Udara :")
GreedyBestFirstSearch(mapMatrixGround, [8, 4], [45, 25], True)
