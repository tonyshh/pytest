price = int(input())
coins = 0
while price >= 25:
    coins += 1
    price = price - 25
while price >= 10:
    coins += 1
    price -= 10
while price >= 5:
    coins += 1
    price -= 5
while 1 <= price < 5:
    coins += 1
    price -= 1
print(coins)
