from collections import deque
n = int(input())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

for _ in range(n):
  체스크기 = int(input())
  체스판 = [[False] * 체스크기 for _ in range(체스크기)]
  현재_위치 = list(map(int, input().split()))
  이동할_위치 = list(map(int, input().split()))

  def bfs():
    체스판[현재_위치[0]][현재_위치[1]] = True
    queue = deque([(현재_위치[0], 현재_위치[1], 0)])
    while queue:
      x, y, cnt = queue.popleft()
      if x == 이동할_위치[0] and y == 이동할_위치[1]:
        return cnt
      for i in range(8):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < 체스크기 and 0 <= my < 체스크기 and not 체스판[mx][my]:   
          queue.append((mx, my, cnt + 1))
          체스판[mx][my] = True
    return -1

  print(bfs())
