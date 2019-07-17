kor, eng, math, sci = map(int, input().split())

if kor<0 or kor>100 or eng<0 or eng>100 or math<0 or math>100 or sci<0 or sci>100:
    print('잘못된 점수')
else:
    average = (kor + eng + math + sci) / 4
    if average >= 80:
        print('합격')
    else:
        print('불합격')
