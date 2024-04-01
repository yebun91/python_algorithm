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

def bfs(edges):
  visited = [False] * len(edges)
  queue = deque([1])
  visited[1] = True
  while queue:
    vertex = queue.popleft()
    result.append(vertex)
    for nextVertex in edges[vertex]:
      if not visited[nextVertex]:
        visited[nextVertex] = True
        queue.append(nextVertex)

bfs(graph)

print(len(result)-1)