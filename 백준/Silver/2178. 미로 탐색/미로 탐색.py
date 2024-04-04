import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

x, y = map(int, input().split())
miro = [list(map(int, (input()))) for _ in range(x)]
check = [[0] * y for _ in range(x)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  queue = deque([(0, 0)])
  check[0][0] = 1

  while queue:
    queueX, queueY = queue.popleft()  
    if queueX == x-1 and queueY == y-1:
      return check[queueX][queueY]
    
    for i in range(4):
      mx, my = queueX + dx[i], queueY + dy[i]
      if mx < 0 or my < 0 or mx >= x or my >= y:
        continue
      if miro[mx][my] == 1 and check[mx][my] == 0:
        queue.append((mx, my))
        check[mx][my] = check[queueX][queueY] + 1
  return -1

print(bfs())