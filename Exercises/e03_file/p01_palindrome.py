# 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수(palindrome)는?
def isPalindrome(a):
    for i in range(len(a)//2):
        if a[i] != a[-1-i]:
            return False
    return True

maxNum = 0
for i in range(100, 1000):
    for k in range(100, 1000):
        if isPalindrome(str(i*k)):
            if i*k > maxNum:
                maxNum = i*k
print(maxNum)