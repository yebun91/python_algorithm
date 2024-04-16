n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  graph[i][i] = 0

for k in range(n):
  for i in range(n):
    for j in range(n):
      if graph[i][k] and graph[k][j]:
        graph[i][j] = 1


for row in graph:
  print(*row)