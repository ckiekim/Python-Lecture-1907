import os
import shutil
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
    filename = '%04d.txt' % filenumber
    file = open(filename, 'w')
    file.write(content)
    file.close()

fileList = os.listdir(PATH)
for filename in fileList:
    # 디렉토리면 처리하지 않고 Loop을 반복
    if os.path.isdir(filename):
        continue

    # 일반 파일이면
    # 파일이름에서 숫자를 구하고, 파일을 읽어서 콘텐츠를 가져온다.
    filenumber = int(filename[0:4])     # '1234.txt'로 부터 1234를 구함
    file = open(filename, 'r')
    content = file.read(1)
    file.close()

    # 원하는 위치에 파일을 이동
    if filenumber <= 3333:
        dirname = 'low'
    elif filenumber <= 6666:
        dirname = 'mid'
    else:
        dirname = 'high'
    dst = dirname + '/' + content + '/' + filename
    shutil.move(filename, dst)

