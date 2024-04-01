import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

n = int(input())
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]

result = []

def createGraph(edges, n):
  graph = [[] for _ in range(n + 1)]
  for edge in edges :
    a, b = edge
    graph[a].append(b)
    graph[b].append(a)

  return graph

graph = createGraph(edges, n)

def bfs(edges, visited):
  queue = deque([1])
  visited[1] = True
  while queue:
    vertex = queue.popleft()
    result.append(vertex)
    for nextVertex in edges[vertex]:
      if not visited[nextVertex]:
        visited[nextVertex] = True
        queue.append(nextVertex)

def dfs(edges, visited, num):
  visited[num] = True
  result.append(num)
  for nextVertex in edges[num]:
    if not visited[nextVertex]:
      dfs(edges, visited, nextVertex)

visited = [False] * len(graph)

# bfs(graph, visited)
dfs(graph, visited, 1)

print(len(result)-1)