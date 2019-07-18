# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
count = int(input('테스트 케이스의 개수> '))
a, b = map(int, input('두 수 입력> ').split())

for i in range(1, count+1):
    print('Case #'+str(i)+':', a, '+', b, '=', a+b)