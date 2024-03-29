# 표준 입력으로 꼭지점 개수(정수)와 선의 길이(정수)가 입력됩니다
# (꼭지점 개수의 입력 범위는 5~10, 선의 길이 입력 범위는 50~150입니다).
# 다음 소스 코드를 완성하여 꼭지점 개수와 선의 길이에 맞는 별이 그려지게 만드세요.
# 별을 그릴 때는 현재 위치부터 오른쪽으로 이동해서 시작해야 하며
# 시계 방향으로 그려야 합니다.
import turtle as t

n, line = map(int, input().split())
t.shape('turtle')
t.speed('fastest')

for i in range(n):
    t.forward(line)
    t.right(360 / n)

t.mainloop()