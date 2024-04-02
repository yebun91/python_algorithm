import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

m, n = map(int, input().split())
edges = []
queue = deque()

for i in range(n):
  tomatos = list(map(int, input().split()))
  isTomato = [index for index, value in enumerate(tomatos) if value == 1]
  if isTomato :
    for j in isTomato :
      queue.append((i, j))
  edges.append(tomatos)

    # 상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]


def bfs():
  days = -1
  while queue: 
    days += 1
    for _ in range(len(queue)): # 처음에 큐에 들어있던 데이터 만큼의 len 반복 천잰데?
      x, y = queue.popleft()
      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0<= ny < m and edges[nx][ny] == 0:
          edges[nx][ny] = 1
          queue.append((nx, ny))

  for row in edges:
    if 0 in row:
      return -1 
    
  return days

print(bfs())