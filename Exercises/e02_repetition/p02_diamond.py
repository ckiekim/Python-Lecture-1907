# 5이상 9이하의 홀수를 입력받아 다이아몬드 형태의 별을 출력하는 프로그램
n = int(input('5이상 9이하의 홀수> '))
height = (n + 1) // 2

for i in range(1, height+1):
    for k in range(height-i):
        print(' ', end='')
    for k in range(i*2-1):
        print('*', end='')
    print()

for i in reversed(range(1, height)):
    for k in range(i, height):
        print(' ', end='')
    for k in range(i*2-1):
        print('*', end='')
    print()