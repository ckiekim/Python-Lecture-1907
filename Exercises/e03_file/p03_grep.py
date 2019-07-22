# Unix grep 명령어
word, filename = input('찾고자 하는 문자열과 파일명> ').split()

lineNo = 1
with open(filename, 'r', encoding='UTF-8') as file:
    for line in file:
        if line.find(word) >= 0:
            print('%3d:' % lineNo, line, end='')
        lineNo += 1
