# 다음의 규칙대로 동작하는 프로그램을 작성하시오.
#    1) 타일판은 5 x 5
#    2) 타일 종류는 1 ~ 4의 네가지로 랜덤값으로 정한 후 타일판 출력
#    3) 가로나 세로로 3개 이상 같은 타일이 연속될 경우
#       타일을 '*'로 바꾸고 타일판 출력
#    4) '*' 타일은 위에서부터 내려오고 빈 칸은 랜덤값으로 채움
#    5) 3), 4) 과정을 '*'이 나오지 않을 때 까지 반복
import constants as c
import random as rd
import util, game

# Program starts here!!!
tile = [[str(rd.randint(1, 4)) for k in range(c.NO_OF_COLUMN)] for i in range(c.NO_OF_ROW)]
print('  Given')
util.printMatrix(tile)

counter = 0
while True:
    counter += 1
    rowResult = []
    wholePung = False
    for i in range(c.NO_OF_ROW):
        pung, start, stop = game.findPung(tile[i])
        if pung:
            wholePung = True
        rowResult.append(util.copyLine(pung, start, stop, tile[i]))

    colResult = []
    tpTile = [list(x) for x in zip(*tile)]
    for i in range(c.NO_OF_ROW):
        pung, start, stop = game.findPung(tpTile[i])
        if pung:
            wholePung = True
        colResult.append(util.copyLine(pung, start, stop, tpTile[i]))
    tpColResult = [list(x) for x in zip(*colResult)]

    if not wholePung:
        break;

    print('   ==>')
    # Merge the result
    for i in range(c.NO_OF_ROW):
        for k in range(c.NO_OF_COLUMN):
            if rowResult[i][k] == '*' or tpColResult[i][k] == '*':
                tile[i][k] = '*'
    util.printMatrix(tile)

    game.collapse(tile)
    print(" Combo", counter)
    util.printMatrix(tile)

print('게임이 끝났습니다.')