price = int(input())
coupon = input()

if coupon == 'Cash3000':
    discount = 3000
if coupon == 'Cash5000':
    discount = 5000

print(price-discount)