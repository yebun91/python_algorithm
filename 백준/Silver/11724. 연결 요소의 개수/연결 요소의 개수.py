import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

maxNum, num = map(int, input().split())
graph = [[] for _ in range(maxNum + 1)]
result = 0

for _ in range(num):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (len(graph))

def dfs(num):
  visited[num] = True
  for nextNum in graph[num]:
    if not visited[nextNum]:
      dfs(nextNum)

def bfs(num):
  global result
  result += 1
  visited[num] = True
  queue = deque([num])
  
  while queue:
    num = queue.popleft()
    for nextNum in graph[num]:
      if not visited[nextNum]:
        visited[nextNum] = True
        queue.append(nextNum)

for i in range(1, maxNum + 1):
  if not visited[i] :
    # result += 1
    # dfs(i)
    bfs(i)

print(result)
