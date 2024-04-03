from collections import deque
n = int(input())
graph = [list(input()) for _ in range(n)]
visitedA = [[False] * n for _ in range(n)]
visitedB = [[False] * n for _ in range(n)]

    # 상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  result = 0
  visitedA[x][y] = True
  queue = deque([(x, y)])
  text = graph[x][y]
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue 
      if graph[nx][ny] == text and not visitedA[nx][ny]:
        result += 1
        visitedA[nx][ny] = True
        queue.append((nx, ny))
  return result

def bfs2(x, y):
  visitedB[x][y] = True
  queue = deque([(x, y)])
  text = graph[x][y]

  if text == 'G': text = 'GR'
  elif text == 'R' : text = 'GR'

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue 
      if graph[nx][ny] in text and not visitedB[nx][ny]:
        visitedB[nx][ny] = True
        queue.append((nx, ny))

z = 0
v = 0

for i in range(n):
  for j in range(n):
    if not visitedA[i][j]:
      bfs(i, j)
      z += 1
    if not visitedB[i][j]:
      bfs2(i, j)
      v += 1

print(z, v)

