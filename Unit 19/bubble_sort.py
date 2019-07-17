# 오름차순으로 버블 소트
# 입력으로 여러개의 숫자를 받음
aList = list(map(int, input('숫자들을 입력하세요> ').split()))
print(aList)

for i in range(0, len(aList)-1):
    for k in range(i+1, len(aList)):
        if aList[i] > aList[k]:            # 부등호가 바뀌면 내림차순이 됨
            aList[i], aList[k] = aList[k], aList[i]

print(aList)