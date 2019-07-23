# 표준 입력으로 정수 한 개가 입력됩니다(입력 값의 범위는 10~30).
# 다음 소스 코드를 완성하여 입력된 정수에 해당하는 피보나치 수가 출력되게 만드세요.
#
# 피보나치 수는 0과 1로 시작하며, 다음 번 피보나치 수는
# 바로 앞의 두 피보나치 수의 합입니다.
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))
