n = int(input())
coins = [500, 100, 50, 10, 5, 1]
charge = 1000 - n
count = 0

for coin in coins:
  count += charge // coin
  charge = charge % coin

print(count)