line = input()
prices = list(map(int, line.split(';')))
prices.sort(reverse=True)

for price in prices:
    print('%9s' % format(price, ','))