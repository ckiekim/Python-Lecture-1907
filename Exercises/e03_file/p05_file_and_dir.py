import os
import random as rd
PATH = 'c:/Temp/Ex04'
os.mkdir(PATH)
os.chdir(PATH)
for dirname in ('low', 'mid', 'high'):
    os.mkdir(PATH + '/' + dirname)
    for num in ('1', '2', '3'):
        os.mkdir(PATH + '/' + dirname + '/' + num)

for i in range(100):
    filenumber = rd.randint(0, 9999)
    content = str(rd.randint(1, 3))
    if filenumber <= 3333:
        dirname = 'low'
    elif filenumber <= 6666:
        dirname = 'mid'
    else:
        dirname = 'high'
    filename = dirname + '/' + content + '/' + '%04d.txt' % filenumber
    file = open(filename, 'w')
    file.write(content)
    file.close()
    