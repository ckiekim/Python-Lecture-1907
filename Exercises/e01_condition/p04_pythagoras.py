# a + b + c = 1000 인 피타고라스 수
# (단, a < b < c 이고 a + b > c)
outerBreak = False
for a in range(1, 333):
    if outerBreak:
        break
    for b in range(a+1, 500):
        c = 1000 - a - b
        if c < b:
            continue
        if a**2 + b**2 == c**2:
            print(a, b, c, a+b+c)
            print(a**2, b**2, c**2)
            outerBreak = True
            break;