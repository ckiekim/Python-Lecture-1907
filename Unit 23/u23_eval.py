from pprint import pprint
col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))
pprint(matrix, indent=2)

def countMines(i, k):
    if matrix[i][k] == '*':
        return '*'
    if i == 0:
        rs = 0
    else:
        rs = i - 1
    if i == col - 1:
        re = col - 1
    else:
        re = i + 1
    if k == 0:
        cs = 0
    else:
        cs = k - 1
    if k == row - 1:
        ce = k
    else:
        ce = k + 1
    count = 0
    for r in range(rs, re+1):
        for c in range(cs, ce+1):
            if matrix[r][c] == '*':
                count += 1
    return count

for i in range(row):
    for k in range(col):
        print(countMines(i, k), end='')
    print()
