# 시저 암호
# 입력 : 화면에서 문자열과 n값
plain, n = input('암호화할 문자열과 N값> ').split()
plain = [c for c in plain]
n = int(n)

LETTER_A = ord('A')     # 변수명을 대문자로 하면 상수(Constant) 취급을 하게 됨.
LETTER_Z = ord('Z')
cypher = []
for letter in plain:
    if ord(letter) + n > LETTER_Z:
        cypher.append(chr(LETTER_A + ord(letter) + n - LETTER_Z - 1))
    else:
        cypher.append(chr(ord(letter) + n))
print(''.join(cypher))
