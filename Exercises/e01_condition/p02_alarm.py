# 45분 일찍 알람 맞추기
hour, min = map(int, input('알람 시각> ').split())

if min >= 45:
    min -= 45
else:
    hour -= 1
    min += 15          # min = min + 60 - 45

print('New alarm time =', hour, min)