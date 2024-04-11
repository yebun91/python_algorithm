computer = int(input())
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
sortedGraph = [[] for _ in range(computer + 1)]
check = [False] * (computer + 1)

for com in graph:
  a, b = com
  sortedGraph[a].append(b)
  sortedGraph[b].append(a)

result = 0

def dfs(n):
  global result
  check[n] = True
  for c in sortedGraph[n]:
    if not check[c]:
      result += 1
      dfs(c)

dfs(1)

print(result)