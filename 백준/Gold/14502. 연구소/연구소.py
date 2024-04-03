import sys
from collections import deque
import itertools
import copy

input = lambda: sys.stdin.readline().strip()

x, y = map(int, input().split())
graph = []
empty = []
virus = []
maxEmpty = 0
visited = [[False] * x for _ in range(y)]

for i in range(x):
  data = list(map(int, input().split()))
  for j, value in enumerate(data):
    if value == 0:
      empty.append((i, j))
    elif value == 2:
      virus.append((i, j))
  graph.append(data)

    # 상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(wall):
  newGraph = copy.deepcopy(graph)
  for i in wall:
    a, b = i
    newGraph[a][b] = 1

  queue = deque(virus)
  
  while queue:
    l, r = queue.popleft()
    for i in range(4):
      nx, ny = l + dx[i], r + dy[i]
      if 0 <= nx < x and 0 <= ny < y and newGraph[nx][ny] == 0:
        newGraph[nx][ny] = 2
        queue.append((nx, ny))

  safe_areas = sum(row.count(0) for row in newGraph)
  return safe_areas

combinations = list(itertools.combinations(empty, 3))

for combination in combinations:
  safe_areas = bfs(combination)
  maxEmpty = max(maxEmpty, safe_areas)

print(maxEmpty)