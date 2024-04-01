from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방문 처리를 위한 배열 초기화
visited = [[False] * m for _ in range(n)]

    # 상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []

def dfs(x, y):
  global area
  visited[x][y] = True
  area += 1

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      continue
    if graph[nx][ny] == 1 and not visited[nx][ny]:
      dfs(nx, ny)


def bfs(x, y):
  queue = deque([(x, y)])
  area = 1  # 현재 그림의 넓이
  visited[x][y] = True

  while queue :
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i] # 현재 위치에서 상하좌우 움직였을때의 위치
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if graph[nx][ny] == 1 and not visited[nx][ny]:
        # 이동한 곳이 1이고 한번도 방문한적 없는 곳이라면
        # 해당 위치를 저장함
        queue.append((nx, ny)) 
        visited[nx][ny] = True
        area += 1 # 넓이를 1 증가시킴

  return area

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1 and not visited[i][j]:
      result.append(bfs(i, j))
      # area = 0
      # dfs(i, j)
      # result.append(area)

      
print(len(result))
print(max(result, default=0))

# dfs는 시간초과 뜨네용