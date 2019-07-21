import binascii as ba
import os

def showHexa(addr, buf, size):
    if addr % 1024 == 0 and addr != 0:
        print()
    print('%08X: ' % addr, end = ' ')
    if size != 16:
        for i in range(size):
            if i == 8:
                print(end=' ')
            print('%02X' % buf[i], end=' ')
        for i in range(size, 16):
            if i == 8:
                print(end=' ')
            print('  ', end=' ')
    else:
        for i in range(size):
            if i == 8:
                print(end=' ')
            print('%02X' % buf[i], end=' ')
    print('  ', end='')
    for i in range(size):
        if i == 8:
            print(end=' ')
        if buf[i] < 0x20 or buf[i] > 0x7e:
            print('.', end='')
        else:
            print(chr(buf[i]), end='')
    print()

filename = input('읽을 파일> ')
fileLength = os.path.getsize(filename)
with open(filename, 'rb') as file:
    count = 0
    for i in range(0, fileLength, 16):
        buf = file.read(16)
        if fileLength - i < 16:
            size = fileLength - i
        else:
            size = 16
        showHexa(i, buf, size)