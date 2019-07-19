# 표준 입력으로 양의 정수 두 개가 입력됩니다.
# 다음 소스 코드를 완성하여 두 숫자의 공약수를 세트 형태로 구하도록 만드세요.
# 단, 최종 결과는 공약수의 합으로 판단합니다.
numA, numB = map(int, input().split())
a = set(i for i in range(1, numA+1) if numA % i == 0)
b = set(i for i in range(1, numB+1) if numB % i == 0)
# print(a)
# print(b)
divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)