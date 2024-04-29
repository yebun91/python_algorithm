from collections import deque

r, c = map(int, input().split())
madang = [list(input()) for _ in range(r)] # '빈필드, #울타리, o양, v늑대

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
check = [[False] * c for _ in range(r)]

def bfs(startx, starty):
  queue = deque([(startx, starty)])
  check[startx][starty] = True
  o = 0
  v = 0

  if madang[startx][starty] == 'v':
    v += 1
  elif madang[startx][starty] == 'o':
    o += 1

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      mx, my = x + dx[i], y + dy[i]
      if 0 <= mx < r and 0 <= my < c and not check[mx][my] and madang[mx][my] != "#":
        queue.append((mx, my))
        check[mx][my] = True
        if madang[mx][my] == 'v':
          v += 1
        elif madang[mx][my] == 'o':
          o += 1  

  if o <= v : o = 0
  else: v = 0

  return [o, v]

totalo = 0
totalv = 0

for i in range(r):
  for j in range(c):
    if madang[i][j] != '#' and not check[i][j]: 
      o, v = bfs(i, j)
      totalo += o
      totalv += v

print(totalo, totalv)