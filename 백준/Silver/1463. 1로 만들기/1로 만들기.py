from collections import deque

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

# def dpFun(n):
#   dp = [0] * (n + 1) # 0부터 n까지의 숫자를 인텍스로 사용하기 위함

#   for i in range(2, n + 1):
#     # 1을 뺀 경우와 비교
#     dp[i] = dp[i - 1] + 1
#     if i % 2 == 0:
#       dp[i] = min(dp[i], dp[i // 2] + 1)
#     if i % 3 == 0:
#       dp[i] = min(dp[i], dp[i // 3] + 1)

#   return dp[n]

def dpFun(n):
  queue = deque([(n, 0)]) 
  visited = set([n])

  while queue:
    number, count = queue.popleft()
    if number == 1:
      return count

    if number % 3 == 0 and number // 3 not in visited:
      visited.add(number // 3)
      queue.append((number // 3, count + 1))
    
    if number % 2 == 0 and number // 2 not in visited:
      visited.add(number // 2)
      queue.append((number // 2, count + 1))
    
    if number - 1 not in visited:
      visited.add(number - 1)
      queue.append((number - 1, count + 1))

print(dpFun(n))