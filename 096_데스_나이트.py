from collections import deque
n = int(input())
nowX, nowY, goX, goY = map(int, input().split())
map = [[ False for _ in range(n)] for _ in range(n)]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs():
  queue = deque([(nowX, nowY, 0)])
  map[nowX][nowY] = 0

  while queue:
    x, y, move = queue.popleft()
    if x == goX and y == goY: 
      return move
    for i in range(6):
      mx, my = x + dx[i], y + dy[i]
      if 0 <= mx < n and 0 <= my < n and not map[mx][my]:
        map[mx][my] = True
        queue.append((mx, my, move + 1))

  return -1
  

print(bfs())