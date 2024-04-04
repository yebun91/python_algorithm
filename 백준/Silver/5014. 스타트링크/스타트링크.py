import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

# f: 스타트링크 건물 층 수, s: 지금 층, g: 스타트링크가 있는 층, 
# u: 위로 u층 갈 수 있음, d: 아래로 d층 갈 수 있음.
# (만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다) 

f, s, g, u, d = map(int, input().split())
button = [u, -d]

def bfs():
  visited = [-1]* (f + 1)
  queue = deque([(s, 0)])
  visited[s] = 0

  while queue:
    floor, count = queue.popleft()
    if floor == g:
      return count
    for i in range(2):
      movedFloor = floor + button[i]
      if movedFloor < 1 or movedFloor > f:
        continue
      elif visited[movedFloor] == -1:
        visited[movedFloor] = count + 1
        queue.append((movedFloor, count + 1))
        
  return "use the stairs"

print(bfs())
