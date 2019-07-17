import random as rd

count = 0
while True:
    dice1 = rd.randint(1, 6)
    dice2 = rd.randint(1, 6)
    print(dice1, dice2)
    count += 1
    if dice1 + dice2 >= 10:
        break

print("Total count =", count)