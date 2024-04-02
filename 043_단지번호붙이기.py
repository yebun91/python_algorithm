import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

n = int(input())
edges = []
for _ in range(n):
  edges.append([int(num) for num in input()])
m = len(edges[0])
result = []
# 방문 처리를 위한 배열 초기화
visited = [[False] * m for _ in range(n)]
    # 상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  point = 1
  visited[x][y] = True
  queue = deque([(x, y)])
  
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if edges[nx][ny] == 1 and not visited[nx][ny]:
        point += 1
        queue.append((nx, ny))
        visited[nx][ny] = True
  result.append(point)

for i in range(n):
  for j in range(m):
    if edges[i][j] == 1 and not visited[i][j]:
      dfs(i, j)

print(len(result))
print(*sorted(result), sep='\n')