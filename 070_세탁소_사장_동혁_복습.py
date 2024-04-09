coins = [25, 10, 5, 1]
n = int(input())
charges = [int(input()) for _ in range(n)]

for charge in charges:
  result = []
  for coin in coins:
    result.append(charge // coin)
    charge = charge % coin

  print(*result)
