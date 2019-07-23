# UNIX wc 명령어
# 구분자는 마침표(‘.’), 쉽표(‘,’), 공백(‘ ‘)
filename = input('파일 이름> ')
wordsDict = dict()

with open(filename, 'r') as file:
    for line in file:
        linewords = line.replace('(', ' ').replace(')', ' ')\
                        .replace(',', ' ').replace('.', ' ').split()
        #print(linewords)
        for word in linewords:
            count = wordsDict.get(word, 0)
            #print(count, end=' ')
            if count == 0:
                wordsDict.setdefault(word, 1)
            else:
                wordsDict.update(dict([(word, count+1)]))

print('총 단어수 =', len(wordsDict))
import operator
wordsList = sorted(wordsDict.items(), key=operator.itemgetter(1), reverse=True)
print('많이 나온 단어')
for i in range(10):
    print(wordsList[i])