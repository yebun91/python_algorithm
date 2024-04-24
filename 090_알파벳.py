import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [False] * 26  # 알파벳 방문 여부 체크
max_length = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y, depth):
  global max_length
  max_length = max(depth, max_length)
  if max_length == 26:
    return
  for i in range(4):
    mx, my = x + dx[i], y + dy[i]
    if 0 <= mx < r and 0 <= my < c:
      index = ord(graph[mx][my]) - ord('A')
      if not visited[index]:
        visited[index] = True
        dfs(mx, my, depth + 1)
        visited[index] = False

index = ord(graph[0][0]) - ord('A')
visited[index] = True

dfs(0, 0, 1)

# def bfs():
#   global max_length
#   queue = deque([(0, 0, {graph[0][0]})])
#   while queue:
#     x, y, visited  = queue.popleft()
#     max_length = max(len(visited), max_length)
#     if max_length == 26:
#       return
#     for i in range(4):
#       mx, my = x + dx[i], y + dy[i]
#       if 0 <= mx < r and 0 <= my < c  and graph[mx][my] not in visited:
#         new_visited = visited.copy()
#         new_visited.add(graph[mx][my])
#         queue.append((mx, my, new_visited))
# bfs()

print(max_length)
