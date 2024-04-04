n = int(input())

# def dpFun(n):
#   result = 0
#   dp = [n]
#   while dp:
#     print(dp)
#     newDp = []
#     for number in dp:
#       if number == 1:
#         return result
#       if number % 3 == 0:
#         newDp.append(number // 3)
#       if number % 2 == 0:
#         newDp.append(number // 2)
#       newDp.append(number - 1)
#       dp = newDp
#     result += 1

def dpFun(n):
  dp = [0] * (n + 1) # 0부터 n까지의 숫자를 인텍스로 사용하기 위함

  for i in range(2, n + 1):
    # 1을 뺀 경우와 비교
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
      dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
      dp[i] = min(dp[i], dp[i // 3] + 1)

  return dp[n]

print(dpFun(n))