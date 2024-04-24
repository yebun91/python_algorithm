
from collections import deque
import sys
sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline().strip()

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
for _ in range(k):
  x, y = map(int, input().split())
  graph[x-1][y-1] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

max_trash = 0

def dfs(x, y):
  graph[x][y] = 0
  size = 1
  for i in range(4):
    mx, my = x + dx[i], y + dy[i]
    if 0 <= mx < n and 0 <= my < m and graph[mx][my] == 1:
      graph[mx][my] = 0
      size += dfs(mx, my)
  return size


def bfs(x, y):
  graph[x][y] = 0
  size = 1
  queue = deque([(x, y)])
  while queue:
    qx, qy = queue.popleft()
    for i in range(4):
      mx, my = qx + dx[i], qy + dy[i]
      if 0 <= mx < n and 0 <= my < m and graph[mx][my] == 1:
        graph[mx][my] = 0
        queue.append((mx, my))
        size += 1

  return size

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      # max_trash = max(max_trash, dfs(i, j))
      max_trash = max(max_trash, bfs(i, j))

print(max_trash)