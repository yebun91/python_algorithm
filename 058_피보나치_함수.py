import sys
def input(): return sys.stdin.readline().strip()

n = int(input())

def fibonacci_count(number):
  dp = [[0, 0] for _ in range(number + 1)]
  if number >= 0: dp[0] = [1, 0]
  if number >= 1: dp[1] = [0, 1]

  for i in range(2, number + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0] 
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1] 
  return dp[number]

for _ in range(n):
  m = int(input())
  result = fibonacci_count(m)
  print(*result)