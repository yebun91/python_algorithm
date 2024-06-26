N = int(input())
P = list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
  for k in range(1, i + 1):
      dp[i] = max(dp[i], dp[i-k] + P[k-1])
print(dp[N])
