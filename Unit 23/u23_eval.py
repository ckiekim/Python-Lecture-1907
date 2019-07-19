# Padding을 이용한 지뢰 찾기
from pprint import pprint
col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))
# pprint(matrix, indent=2)
padding = [['.'] * (col+2) for i in range(row+2)]
for r in range(1, row + 1):
    for c in range(1, col + 1):
        padding[r][c] = matrix[r-1][c-1]
# pprint(padding, indent=2)

def countMines(i, k):
    if padding[i+1][k+1] == '*':
        return '*'
    count = 0
    for r in range(i, i+3):
        for c in range(k, k+3):
            if padding[r][c] == '*':
                count += 1
    return count

for i in range(row):
    for k in range(col):
        print(countMines(i, k), end='')
    print()
