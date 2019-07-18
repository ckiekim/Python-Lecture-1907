# 연도를 입력으로 받아 윤년인지 아닌지를 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
year = int(input('연도 입력> '))

if year % 4 == 0:
    if year % 400 == 0:
        print(year, '년은 윤년입니다.')
    elif year % 100 == 0:
        print(year, '년은 윤년이 아닙니다.')
    else:
        print(year, '년은 윤년입니다.')
else:
    print(year, '년은 윤년이 아닙니다.')
