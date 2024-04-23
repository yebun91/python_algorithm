from collections import deque

M, N, n = map(int, input().split())
graph = [[0] * N for _ in range(M)]
for _ in range(n):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(y1, y2):
    for j in range(x1, x2):
      graph[i][j] = 1

result = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
  queue = deque([(x, y)])
  graph[x][y] = 2
  result = 1

  while queue:
    a, b = queue.popleft()
    for i in range(4):
      ax, by = a + dx[i], b + dy[i]
      if 0 <= ax < M and 0 <= by < N and graph[ax][by] == 0:
        graph[ax][by] = 2
        result += 1
        queue.append((ax, by))

  return result

for i in range(M):
  for j in range(N):
    if graph[i][j] == 0:
      result.append(bfs(i, j)) 

result.sort()
print(len(result))
print(*result)
