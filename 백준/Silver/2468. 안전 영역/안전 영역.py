import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def bfs(x, y, rain):
  check[x][y] = True
  queue = deque([(x, y)])
  while queue:
    popX, popY = queue.popleft()
    for i in range(4):
      nextX, nextY = popX + dx[i], popY + dy[i]
      if 0 <= nextX < n and 0 <= nextY < n and not check[nextX][nextY] and graph[nextX][nextY] > rain:
        queue.append((nextX, nextY))
        check[nextX][nextY] = True

for k in range(0, 101):
  a = 0
  check = [[False] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if not check[i][j] and graph[i][j] > k :
        a += 1
        bfs(i, j, k)
    
    result = max(result, a)

print(result)