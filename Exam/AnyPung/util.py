def printMatrix(mat):
    for i in range(len(mat)):
        for k in range(len(mat[i])):
            print(mat[i][k], end=' ')
        print()

def copyLine(pung, start, stop, line):
    newLine = line.copy()
    if pung:
        for i in range(start, stop+1):
            newLine[i] = '*'
    return newLine
