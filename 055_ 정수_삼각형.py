import sys
input = lambda: sys.stdin.readline().strip()

n = int(input()) 
numbers = [list(map(int, input().split())) for _ in range(n)]  

dp = [[0 for _ in range(len(numbers[i]))] for i in range(n)]
dp[0] = numbers[0]

for i in range(1, n):
  for j in range(len(numbers[i])):
    if j == 0:
      # 왼족 끝일 경우 더하는 경우의 수가 하나 뿐임
      dp[i][j] = dp[i-1][j] + numbers[i][j]
    elif j == len(numbers[i]) -1:
      # 오른쪽 끝도 마찬가지!
      dp[i][j] = dp[i-1][j-1] + numbers[i][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + numbers[i][j]
      
print(max(dp[n-1]))
