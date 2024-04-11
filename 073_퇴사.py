n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]
# [걸리는 날짜, 수입]
dp = [0] * (n + 1)

for i in range(n):
  # 시작할 일이 퇴사하기 전에 끝낼 수 있다면
  if i + work[i][0] <= n:
    # 일이 끝나는 날짜 = max(기존의 dp, dp[i]일까지 얻을 수 있는 최대수익 + 이번일을 통해 얻는 수익)
    dp[i + work[i][0]] = max(dp[i + work[i][0]], dp[i] + work[i][1])
  dp[i + 1] = max(dp[i + 1], dp[i])
  print(dp)

print(dp[n])