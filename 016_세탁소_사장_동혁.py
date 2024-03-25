n = int(input())
coins = [25, 10, 5, 1]

for _ in range(n):
  charge = int(input())
  result = [0, 0, 0, 0]
  for i in range(len(coins)):
    result[i] = charge // coins[i]
    charge = charge % coins[i]
  
  print(*result)

