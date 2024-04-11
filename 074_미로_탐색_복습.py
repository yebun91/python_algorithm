from collections import deque

x, y = map(int, input().split())
graph = [list(map(int, input())) for _ in range(x)]
check = [[False] * y for _ in range(x)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
  queue = deque([(0, 0)]) 
  check[0][0] = True
  while queue:
    queueX, queueY = queue.popleft()
    for i in range(4):
      mx, my = queueX + dx[i], queueY + dy[i]
      if 0 <= mx < x and 0 <= my < y and not check[mx][my] and graph[mx][my] == 1:
        queue.append((mx, my))
        check[mx][my] = True
        graph[mx][my] = graph[queueX][queueY] + 1 

bfs()

if graph[x-1][y-1] <= 1: print(-1)
else: print(graph[x-1][y-1])