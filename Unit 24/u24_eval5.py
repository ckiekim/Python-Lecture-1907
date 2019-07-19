import string
words = input().split()

count_the = 0
for word in words:
    word = word.strip(string.punctuation)
    if word == 'the':
        count_the += 1
print(count_the)