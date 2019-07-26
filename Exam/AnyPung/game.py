import constants as c
import random as rd

def findPung(line):  # 한 라인을 매개변수로 받아, 결과, 시작, 끝 인덱스 반환
    start = 0
    stop = 0
    pung = False
    for i in range(c.NO_OF_COLUMN - 2):
        if line[i] != line[i+1] or line[i+1] != line[i+2]:
            continue
        pung = True
        start = i
        stop = i+2
        if i == c.NO_OF_COLUMN - 3:
            break
        if line[i+2] != line[i+3]:
            break
        stop = i+3
        if i == c.NO_OF_COLUMN - 4:
            break
        if line[i+3] == line[i+4]:
            stop = i+4
        break
    return pung, start, stop

def collapse(tile):
    for i in range(c.NO_OF_ROW):
        for k in range(c.NO_OF_COLUMN):
            if tile[i][k] == '*':
                if i == 0:
                    tile[i][k] = str(rd.randint(1, 4))
                elif i == 1:
                    tile[i][k] = tile[i-1][k]
                    tile[i-1][k] = str(rd.randint(1, 4))
                elif i == 2:
                    tile[i][k] = tile[i - 1][k]
                    tile[i - 1][k] = tile[i - 2][k]
                    tile[i - 2][k] = str(rd.randint(1, 4))
                elif i == 3:
                    tile[i][k] = tile[i - 1][k]
                    tile[i - 1][k] = tile[i - 2][k]
                    tile[i - 2][k] = tile[i - 3][k]
                    tile[i - 3][k] = str(rd.randint(1, 4))
                else:
                    tile[i][k] = tile[i - 1][k]
                    tile[i - 1][k] = tile[i - 2][k]
                    tile[i - 2][k] = tile[i - 3][k]
                    tile[i - 3][k] = tile[i - 4][k]
                    tile[i - 4][k] = str(rd.randint(1, 4))
