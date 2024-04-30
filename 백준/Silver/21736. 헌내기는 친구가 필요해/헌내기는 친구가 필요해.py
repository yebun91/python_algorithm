from collections import deque

n, m = map(int, input().split())
map = []
start = []

for i in range(n):
  line = list(input())
  map.append(line)
  for j in range(len(line)):
    if line[j] == 'I':
      start.append(i)
      start.append(j)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
  result = 0
  check = [[False] * m for  _ in range(n)]
  check[start[0]][start[1]] = True
  queue = deque([(start[0], start[1])])

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      mx, my = x + dx[i], y + dy[i]
      if 0 <= mx < n and 0 <= my < m and not check[mx][my] and map[mx][my] != "X":
        check[mx][my] = True
        queue.append((mx, my))
        if map[mx][my] == "P": result += 1
  if result == 0 :
    return 'TT'
  return result

print(bfs())